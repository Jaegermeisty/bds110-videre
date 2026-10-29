"""A2 poster with vector text and 4x screenshots of the actual app."""
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A2
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'output/pdf'; OUT.mkdir(parents=True,exist_ok=True)
pdfmetrics.registerFont(TTFont('Arial','/System/Library/Fonts/Supplemental/Arial.ttf'))
pdfmetrics.registerFont(TTFont('ArialBold','/System/Library/Fonts/Supplemental/Arial Bold.ttf'))
W,H=A2
INK='#18283b';BLUE='#234fd0';MUTED='#596675';LINE='#dce2e8';BG='#f4f5f3'
c=canvas.Canvas(str(OUT/'BDS110-Videre-A2.pdf'),pagesize=A2,pageCompression=1)
c.setTitle('Toget er forsinket. Men vet du hva du skal gjøre? | BDS110 Showcase')
c.setAuthor('Gruppe 19 · BDS110 · Universitetet i Stavanger')
c.setSubject('Uoffisiell studentprototype om handlingsrettet avvikskommunikasjon på Jærbanen')
def rect(x,y,w,h,color,r=0,stroke=None):
 c.setFillColor(HexColor(color));c.setStrokeColor(HexColor(stroke or color))
 if r:c.roundRect(x,y,w,h,r,stroke=bool(stroke),fill=1)
 else:c.rect(x,y,w,h,stroke=bool(stroke),fill=1)
def text(x,y,t,size=12,bold=False,color=INK):
 c.setFillColor(HexColor(color));c.setFont('ArialBold' if bold else 'Arial',size);c.drawString(x,y,t)
def para(x,top,t,width,size=15,color=MUTED,bold=False,leading=None):
 style=ParagraphStyle('p',fontName='ArialBold' if bold else 'Arial',fontSize=size,leading=leading or size*1.45,textColor=HexColor(color))
 p=Paragraph(t,style);_,height=p.wrap(width,1000);p.drawOn(c,x,top-height);return top-height
def line(y,x1=52,x2=W-52):
 c.setStrokeColor(HexColor(LINE));c.setLineWidth(.7);c.line(x1,y,x2,y)
rect(0,0,W,H,BG)
text(52,H-57,'videre.',30,True)
text(208,H-51,'BDS110  /  DIGITAL KOMMUNIKASJON',11,True,MUTED)
text(W-290,H-51,'UIS · GRUPPE 19 · 03.11.2026',10,True,MUTED)
line(H-80)
text(52,H-123,'EN BEDRE REISEBESKJED',11,True,BLUE)
text(52,H-194,'Toget er forsinket.',58,True)
text(52,H-256,'Men vet du hva du skal gjøre?',58,True,BLUE)
para(52,H-284,'Hvordan kan Go-Ahead Nordic forbedre digital kommunikasjon<br/>ved avvik på Jærbanen?',W-104,21,INK,leading=28)
# Problem and proposal, distinguished from verified effects.
y=H-437
rect(52,y,W-104,91,'#ffffff',12)
text(72,y+65,'UTFORDRINGEN I GRUPPEOPPGAVEN',10,True,MUTED)
para(72,y+51,'Pendlere trenger mer enn en avviksmelding.<br/>De trenger å forstå konsekvensen for sin reise.',490,16,INK)
text(628,y+65,'VÅRT FORSLAG',10,True,BLUE)
para(628,y+51,'En fast budskapsstruktur, samordnet informasjon<br/>og personlige varsler for berørte reisende.',480,16,INK)
# Three genuine app screens, with surrounding rounded device outlines.
col=(W-104-56)/3
screenw=col-12
screenh=screenw*756/370
screen_top=H-506
steps=[('01','Før avviket','app-normal.png','En personlig pendlerreise.','Reisen og varslingen er samlet på ett sted.'),('02','Når planen endrer seg','app-forsinkelse.png','Tre spørsmål. Tre tydelige svar.','Avgang, konsekvens og neste steg i samme beskjed.'),('03','Et neste steg','app-alternativer.png','Åpenhet om det vi ikke vet.','Alternativer merkes tydelig når de er ubekreftet.')]
for i,(n,title,image,caption,body) in enumerate(steps):
 x=52+i*(col+28)
 text(x,screen_top+30,n,12,True,BLUE);text(x+30,screen_top+30,title,18,True)
 rect(x-1,screen_top-screenh-7,col+2,screenh+14,'#20262d',31)
 c.saveState();p=c.beginPath();p.roundRect(x+6,screen_top-screenh,screenw,screenh,25);c.clipPath(p,stroke=0,fill=0)
 c.drawImage(ImageReader(str(ROOT/'output/screenshots'/image)),x+6,screen_top-screenh,width=screenw,height=screenh,mask='auto')
 c.restoreState()
 captiontop=screen_top-screenh-27
 text(x,captiontop,caption,14,True)
 para(x,captiontop-12,body,col,12.5,MUTED,leading=18)
# Theory section.
base=screen_top-screenh-105
line(base+18)
text(52,base-10,'DESIGNVALG MED FAGLIG FORANKRING',11,True,BLUE)
theory=[('Strategiske budskap','Cornelissen (2020), kap. 6','Vi konkretiserer anbefalingen i tre svar: Hva har skjedd? Hva betyr det for reisen din? Hva kan du gjøre nå?'),('Integrert kommunikasjon','Cornelissen (2020), kap. 2','App og SMS bruker samme oppdatering. Samordning skal motvirke motstridende beskjeder mellom kanalene.'),('Interessenter og målgrupper','Cornelissen (2020), kap. 4 og 6','Berørte pendlere prioriteres ut fra et legitimt, tidskritisk informasjonsbehov. Varslene knyttes til deres egen avgang.')]
for i,(title,ref,body) in enumerate(theory):
 x=52+i*(col+28)
 text(x,base-43,title,17,True)
 text(x,base-65,ref,11,False,BLUE)
 para(x,base-82,body,col,14.5,MUTED,leading=21)
# Takeaway.
by=base-222
rect(52,by,W-104,74,INK,10)
text(73,by+45,'MÅLET: FRA USIKKERHET TIL ET INFORMERT VALG',10,True,'#cbd8f4')
text(73,by+19,'God avvikskommunikasjon skal hjelpe den reisende videre.',23,True,'#ffffff')
# Source and responsibility footer.
fy=by-26
text(52,fy,'KILDEGRUNNLAG',9,True,MUTED)
para(52,fy-10,'Gruppe 19 (2026). Go Ahead Nordic Kommunikasjonsutfordring, s. 3–9. BDS110, Universitetet i Stavanger.<br/>Cornelissen, J. (2020). Corporate communication: A guide to theory and practice (6. utg.). SAGE. Kap. 2, 4 og 6.',W-104,10,MUTED,leading=14)
para(52,fy-50,'Uoffisiell konseptprototype, ikke et Go-Ahead-produkt. Alle reiser, tider, avvik og varsler er fiktive. Ingen samarbeid eller godkjenning er forutsatt.<br/>Dette er et designforslag basert på gruppeoppgaven. Effekten på reisende er ikke brukertestet. Skjermbildene er hentet fra den fungerende prototypen.',W-104,10,MUTED,leading=14)
para(52,fy-88,'Daniel Leite · Mathias Jæger-Pedersen · Rebekka Heida Roberstdottir · Mayvelline Padillo · Sander Jung · Yngve Grødem',W-104,9,MUTED,leading=13)
assert fy-110>32,fy
c.showPage();c.save()
r=PdfReader(OUT/'BDS110-Videre-A2.pdf');assert len(r.pages)==1
assert abs(float(r.pages[0].mediabox.width)-W)<.1
print(f'A2 PDF: {W:.2f} × {H:.2f} pt; lower content boundary {fy-110:.1f} pt')
