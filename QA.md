# Kvalitetskontroll

Utført 29. oktober 2026 i Chrome 156 med Playwright.

## Funksjon og drift

- Normal reise → ukjent forsinkelse → alternativer → tilbake → ny estimert avgang → nullstilling.
- Varsler på/av, tom varslingsliste og åpning av personlig varsel.
- Ekstra vurdering av ubekreftet alternativ kan åpnes og lukkes.
- SMS-eksempelet samsvarer med begge avviksoppdateringer. Dialogen kan lukkes med knapp og Escape.
- Ingen JavaScript-feil registrert.
- Produksjonsfil åpnet direkte med `file://` i en nettleserkontekst med offline-modus. Ingen eksterne HTTP-forespørsler. Lokal server testet separat.
- Tilstand ligger bare i minnet; nullstilling og oppfrisking gir en gjentakbar demonstrasjon.

## Layout og tilgjengelighet

Skjermbilder fra 1366 × 768, 1920 × 1080, 768 × 1024, 390 × 844 og 320 × 740. Ingen horisontal dokumentoverflyt. Hele avviksmeldingen og primærhandlingen passer i telefonen på begge laptopstørrelser. På den smaleste mobilen rulles appinnholdet; navigasjon og demonstrasjonskontroller ligger utenfor rulleområdet.

Desktop, mobil og faktiske appvisninger er inspisert visuelt. Plakatbildene tas med redusert bevegelse, slik at overgangens innfading ikke gjør dem bleke. Norsk æ, ø og å er visuelt kontrollert. Mørk brødtekst, blå handlinger og varseltekst bruker høy kontrast mot lyse flater; status formidles også med tekst og symboler.

Appkontroller har 44 CSS-piksler minimumshøyde; presentatørkontrollene på mobil er mindre og ligger utenfor appen. Tastaturfokus er synlig, bryteren har `role=switch`, tilstander har tekstetiketter og simulerte hendelser annonseres i et `aria-live`-område. Redusert bevegelse støttes.

Dette er ikke en full WCAG-revisjon. Safari, Firefox, en fysisk iPhone og skjermleser er ikke separat testet. Ingen brukertest med reisende er gjennomført.

## Plakat

- Én side på 420 × 594 mm (A2 stående), verifisert med PDF-leser.
- Innebygde skrifter, vektortekst og ekte appskjermbilder i fire ganger CSS-oppløsningen.
- Eksportert til 300 dpi PNG: 4961 × 7016 piksler.
- PDF-en rendret med Poppler og kontrollert visuelt for linjebrudd, lesbarhet, marger og avklipping.
- Studentforbehold, kildehenvisninger og skille mellom forslag og målt effekt står på plakaten.

Maskinlesbar rapport: `output/test-report.json`. Gjennomførte rettinger: telefonens høyde/desktopmarger, innholdsoverflyt på avviksskjermen, plass til bunntekst i alternativvisningen og animasjonsfri skjermbildefangst.
