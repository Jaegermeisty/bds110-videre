# Videre – BDS110 Showcase

En ferdig, lokal konseptprototype om tydeligere informasjon ved avvik på Jærbanen. Laget for gruppe 19s Showcase 3. november 2026. Hele opplevelsen er på norsk bokmål.

## Start uten installasjon

1. Åpne mappen `dist`.
2. Dobbeltklikk `index.html`. Appen åpnes i nettleseren.
3. Bruk gjerne fullskjerm. På Mac: Ctrl + Cmd + F.
4. Trykk **Simuler forsinkelse** under telefonen. Bruk **Se alternative reiser** inne i appen.
5. Trykk på pilen som går rundt for å nullstille før neste besøkende.

Du trenger verken Node, Python, internett, konto eller en server for å demonstrere appen. Produksjonsfilen inneholder alle stilregler og ikoner. Systemskrifter brukes lokalt. Ingen informasjon sendes eller lagres. Oppfrisking av siden starter på nytt.

På mobil vises appen uten telefonramme. Presentatørkontrollene ligger under appen. På små skjermer kan innholdet inne i appen rulles.

## Det dere skal bruke på standen

- `dist/index.html` – den ferdige appen.
- `output/pdf/BDS110-Videre-A2.pdf` – én side, A2 stående, 420 × 594 mm.
- `output/pdf/BDS110-Videre-A2.png` – 300 dpi, 4961 × 7016 piksler.
- `output/screenshots/` – appvisninger i høy oppløsning og desktop-/mobilbilder.
- `PRESENTATORGUIDE.md` – demonstrasjon på 2–3 minutter og spørsmål dere kan få.
- `research/KILDEGRUNNLAG.md` – kildegrunnlag og skillet mellom analyse, forslag og simulering.
- `output/test-report.json` og `QA.md` – gjennomførte kontroller og avgrensninger.

Skriv ut PDF-en i **faktisk størrelse / 100 %** på A2, stående. Unngå «tilpass til side» dersom trykkeriet støtter riktig format. Layouten har innvendige marger og krever ikke beskjæring. Det er en vanlig PDF med innebygde skrifter og RGB-farger, ikke en PDF/X-fil med trykkerispesifikk CMYK-profil. PNG-en er en forhåndsvisning; PDF-en er originalen til utskrift.

## Demonstrasjonens tilstander

| Tid | Hva skjer? | Hva formidles? |
| --- | --- | --- |
| 07.32 | Nora ser sin planlagte reise 07.42–07.59 | Reisen er i rute. Varsler er forhåndsvalgt i scenarioet. |
| 07.35 | Presentatøren simulerer signalfeil | Berørt avgang, konsekvens, ukjent avgangstid og ny beskjed senest 07.40. |
| Alternativer | Nora undersøker veien videre | Neste rutetid 08.12 er ubekreftet. Ingen bekreftet buss for tog. |
| 07.40, valgfritt | Presentatøren viser en ny oppdatering | Anslått avgang 07.57 og ankomst 08.14; ny beskjed senest 07.45. Anslagene er ikke bekreftet. |

Klokken styres av presentatøren. Dette er ikke en automatisk tidslinje. Ingen reelle avganger, avvik eller SMS-meldinger hentes eller sendes.

## Utvikling og vedlikehold

Løsningen er bevisst bygget uten kjøretidsavhengigheter. Det gir en enkel offline-leveranse for tre avgrensede hovedvisninger. React, Vite og Tailwind er derfor ikke nødvendig her.

- `src/index.html`: innramming og desktopinnhold.
- `src/style.css`: app, telefonramme, responsivitet og utsnitt.
- `src/app.js`: tilstander, norske tekster og interaksjon. App og SMS leser de samme oppdateringsdataene.
- `scripts/build.mjs`: setter kildefilene sammen til én selvstendig fil.
- `scripts/test.mjs`: Playwright-test og skjermbilder.
- `scripts/poster.py`: reproduserbar plakat med vektortekst og ekte appskjermbilder.

For å bygge på nytt med Node: `npm run build`.

Valgfri lokal server: `npm start` (krever Python 3), og åpne `http://localhost:4173`. Stopp med Ctrl+C. Porten brukes bare lokalt.

For å kjøre testene på en annen maskin: installer Playwright (`npm install --no-save playwright`), start den lokale serveren og kjør `npm test`. Testen bruker Chrome fra `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`; angi `CHROME_PATH` for en annen installasjon. Den leverte testrapporten ble laget med Codex' lokale Playwright-runtime.

Plakatgenerering krever Python-pakkene `reportlab`, `pypdf` og `Pillow`, samt Arial-skriftene som er installert på macOS. `python3 scripts/poster.py` lager PDF-en. `pdftoppm -r 300 -singlefile -png output/pdf/BDS110-Videre-A2.pdf output/pdf/BDS110-Videre-A2` lager PNG-en. Appskjermbildene tas først av testen i fire ganger CSS-oppløsningen.

Dette er en uoffisiell studentprototype og et designforslag, ikke et produkt fra Go-Ahead Nordic. Effekten på faktiske reisende er ikke undersøkt.

## GitHub og nettside

- Nettside: https://jaegermeisty.github.io/bds110-videre/
- Kildekode: https://github.com/Jaegermeisty/bds110-videre
- Lokal Git-mappe: `showcase` i BDS110-mappen.
- Git bruker kontoens eksisterende SSH-tilkobling. Ingen ny innlogging kreves for `git push` fra denne maskinen.

Prosjektet publiseres med GitHub Pages fra `main`-grenens `docs`-mappe. `npm run build` oppdaterer både den lokale produksjonsfilen i `dist` og nettsiden i `docs`.

Oppdater nettsiden etter en endring:

```sh
npm run build
git add src scripts docs dist README.md
git commit -m "Oppdater prototypen"
git push
```

GitHub publiserer den nye versjonen etter push. Pensumfiler, midlertidige tekstuttrekk og lokale leveransefiler i `output` holdes utenfor repositoryet. Nettsiden inneholder kun selve konseptprototypen.
