import {createRequire} from 'node:module';
import {fileURLToPath} from 'node:url';
import {mkdir,writeFile} from 'node:fs/promises';
import assert from 'node:assert/strict';
const require=createRequire(import.meta.url);
let playwright;try{playwright=require('playwright')}catch{playwright=require('/Users/mathiasjaeger-pedersen/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright')}
const browser=await playwright.chromium.launch({headless:true, executablePath:process.env.CHROME_PATH || "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"});
const root=new URL('../',import.meta.url),output=new URL('output/screenshots/',root);
await mkdir(output,{recursive:true});
const url=new URL('dist/index.html',root).href;
const context=await browser.newContext({viewport:{width:1366,height:768},deviceScaleFactor:2,reducedMotion:"reduce"});
const page=await context.newPage();
const errors=[];page.on('pageerror',e=>errors.push(e.message));
let external=0;page.on('request',r=>{if(/^https?:/.test(r.url()))external++});
await context.setOffline(true);
await page.goto(url);
await assertText('Din neste reise');assert.match(await page.locator('#story-title').innerText(),/Nora skal/);
assert.equal(await page.locator('[aria-current="step"]').getAttribute('id'),'step-0');
await page.screenshot({path:fileURLToPath(new URL('01-desktop-normal.png',output))});
await page.getByRole('switch').click();assert.equal(await page.getByRole('switch').getAttribute('aria-checked'),'false');
await page.locator('#nav-notifications').click();await assertText('Varsler er slått av');
await page.getByRole('switch').click();await assertText('Ingen nye varsler');
await page.getByRole('button',{name:'Min reise',exact:true}).click();
await page.getByRole('button',{name:'Simuler forsinkelse'}).click();await assertText('Din reise er berørt');await assertText('Ny avgangstid er ukjent');assert.match(await page.locator('#story-title').innerText(),/for Nora/);assert.equal(await page.locator('[aria-current="step"]').getAttribute('id'),'step-1');await assertText('07.40');
await page.screenshot({path:fileURLToPath(new URL('02-desktop-forsinkelse.png',output))});
await page.getByRole('button',{name:'Se SMS'}).click();assert.equal(await page.locator('#channels-dialog').evaluate(el=>el.open),true);assert.match(await page.locator('#sms').textContent(),/07.42.*07.40/);await page.keyboard.press('Escape');
await page.locator('#nav-notifications').click();await assertText('L5 kl. 07.42 er forsinket');await page.locator('.notification-item').click();await assertText('Din reise er berørt');
await page.getByRole('button',{name:'Se alternative reiser'}).click();await assertText('Veien videre');assert.match(await page.locator('#story-title').innerText(),/gjøre nå/);assert.equal(await page.locator('[aria-current="step"]').getAttribute('id'),'step-2');await assertText('Ikke bekreftet');
await page.getByRole('button',{name:'Hva bør jeg vurdere?'}).click();await assertText('Det er ikke avklart om togbilletten gjelder');await page.getByRole('button',{name:'Skjul vurderingen'}).click();
await page.screenshot({path:fileURLToPath(new URL('03-desktop-alternativer.png',output))});
await page.getByRole('button',{name:'Tilbake til reiseoppdateringen'}).click();await page.getByRole('button',{name:'Vis oppdatering kl. 07.40'}).click();await assertText('Anslått avgang 07.57');assert.match(await page.locator('#story-title').innerText(),/07.57/);await assertText('07.45');
await page.getByRole('button',{name:'Se SMS'}).click();assert.match(await page.locator('#sms').textContent(),/07.57.*07.45/);await page.getByRole('button',{name:'Lukk SMS'}).click();
await page.getByRole('button',{name:'Nullstill demonstrasjonen'}).click();await assertText('Din neste reise');assert.equal(await page.getByRole('switch').getAttribute('aria-checked'),'true');
// Additional controls: close icon, top back button and reset from alternatives.
await page.getByRole('button',{name:'Se SMS'}).click();await page.getByRole('button',{name:'Lukk SMS'}).click();
await page.getByRole('button',{name:'Simuler forsinkelse'}).click();await page.getByRole('button',{name:'Se alternative reiser'}).click();
await page.locator('.back').click();await assertText('Din reise er berørt');
await page.getByRole('button',{name:'Se alternative reiser'}).click();await page.getByRole('button',{name:'Nullstill demonstrasjonen'}).click();await assertText('Din neste reise');
for(const size of [{width:1366,height:768},{width:1920,height:1080},{width:768,height:1024},{width:390,height:844},{width:320,height:740}]){
 await page.setViewportSize(size);await page.goto(url);assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true,`overflow ${size.width}`);
 await page.getByRole('button',{name:'Simuler forsinkelse'}).click();
 const screen=page.locator('#screen');const bounds=await screen.boundingBox();assert(bounds.width<=size.width);
 const scroll=await page.locator('#app-scroll').evaluate(el=>({client:el.clientHeight,scroll:el.scrollHeight}));
 console.log('Layout',size,scroll);if(size.width===1366||size.width===1920)assert.equal(scroll.scroll<=scroll.client,true,'Disruption must fit desktop phone');
 if(size.width>=900)assert.equal(await page.evaluate(()=>document.documentElement.scrollHeight<=innerHeight+2),true,'Desktop must fit height');
 await page.screenshot({path:fileURLToPath(new URL(`layout-${size.width}.png`,output)),fullPage:true});
}
const printContext=await browser.newContext({viewport:{width:370,height:756},deviceScaleFactor:4,reducedMotion:"reduce"});const printPage=await printContext.newPage();
for(const [name,query] of [['app-normal',''],['app-forsinkelse','&phase=1'],['app-alternativer','&phase=1&view=alternatives'],['app-oppdatering','&phase=2']]){
 await printPage.goto(url+'?app=1'+query);await printPage.screenshot({path:fileURLToPath(new URL(name+'.png',output))});
}
await context.setOffline(false);await page.goto('http://localhost:4173');await assertText('Din neste reise');
assert.equal(errors.length,0,errors.join('\n'));assert.equal(external,1,'Exactly one HTTP request for optional local server check');
const report={passed:true,date:'2026-10-29',checks:['Normal reise, forsinkelse, estimert oppdatering og nullstilling','Alternative reiser, vurderingsdetaljer og tilbakeknapper','Varsler av/på, tom visning og personlig varsel','Samordnet SMS ved begge avviksoppdateringer, dialog og Escape','Kort sidetekst og aktivt steg følger reisen, forsinkelsen og alternativene','1366×768, 1920×1080, 768×1024, 390×844 og 320×740 uten horisontal overflow','Ingen JavaScript-feil','Direkte filåpning i offline-kontekst; ingen eksterne ressurser','Lokal HTTP-server svarer'],browser:await browser.version()};
await writeFile(new URL('output/test-report.json',root),JSON.stringify(report,null,2));console.log(JSON.stringify(report,null,2));await browser.close();
async function assertText(text){console.log('Check:',text);await page.getByText(text,{exact:false}).first().waitFor({state:'visible',timeout:6000});}
