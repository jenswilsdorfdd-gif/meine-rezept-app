import streamlit as st

# Datenbank-Initialisierung mit allen 34+ Rezepten
if 'recipes' not in st.session_state:
    st.session_state.recipes = {
        "Drumsticks San Francisco Style": {
            [cite_start]"Zutaten": ["1,5 kg Hühnerbeine", "75 ml Sojasauce", "1 EL Reisessig", "2 EL trockener Sherry", "Saft einer Orange", "5 cm Orangenschale", "1 EL brauner Zucker", "1 Sternanis", "1 EL Maisstärke", "50 ml lauwarmes Wasser", "1 EL Ingwer", "1/2 Knoblauchzehe", "1-2 Chilischoten [cite: 146-158]"],
            [cite_start]"Werkzeuge": ["Topf", "Rührwerkzeug", "Backblech", "Pinsel [cite: 160, 165, 166]"],
            [cite_start]"Anleitung": ["Sauce aufkochen [cite: 160][cite_start]", "Stärke einrühren und 1 Min. kochen [cite: 161][cite_start]", "Ingwer und Knoblauch unterrühren [cite: 162][cite_start]", "10-15 Min. ziehen lassen [cite: 164][cite_start]", "Drumsticks mit Sauce bestreichen [cite: 165][cite_start]", "Bei 200°C 30-40 Min. backen [cite: 168]"]
        },
        "Caesar's Salad": {
            [cite_start]"Zutaten": ["1 Römersalat", "100 g Parmesan", "Toastbrot, Knoblauch, Olivenöl", "Dressing: Sardellen, 4-5 Knoblauchzehen, Balsamico, Dijonsenf, Worcestersauce, Eigelb, Zitronensaft [cite: 20-31]"],
            [cite_start]"Werkzeuge": ["Pürierstab", "Pfanne", "Salatschüssel [cite: 33, 35]"],
            [cite_start]"Anleitung": ["Dressing pürieren und mit Olivenöl aufgießen [cite: 33][cite_start]", "Salat schneiden und vermischen [cite: 34][cite_start]", "Croutons in Pfanne rösten [cite: 35][cite_start]", "Mit Parmesan und Croutons bestreuen [cite: 34, 35]"]
        },
        "1-2-3-Teig": {
            "Zutaten": ["200 g Butter", "1 Pck. [cite_start]Vanillezucker", "150 g Zucker", "1 Ei", "325 g Mehl", "100 g Speisestärke [cite: 36-42]"],
            [cite_start]"Werkzeuge": ["Handrührgerät (Knethaken)", "Arbeitsplatte", "Nudelholz", "Ausstechformen", "Backblech [cite: 46, 47]"],
            [cite_start]"Anleitung": ["Trockene Zutaten mischen [cite: 45][cite_start]", "Butter und Ei unterkneten [cite: 45, 46][cite_start]", "Teig ausrollen und ausstechen [cite: 47]", "Bei 200°C ca. [cite_start]12 Min. backen [cite: 48]"]
        },
        "Schneller Käsekuchen (ohne Boden)": {
            "Zutaten": ["1 kg Magerquark", "125 g weiche Butter", "200 g Zucker", "4 Eier", "1 Pck. Vanillinzucker", "1 Pck. [cite_start]Puddingpulver", "2 EL Grieß", "Saft einer Zitrone [cite: 75-82]"],
            [cite_start]"Werkzeuge": ["Schüssel", "Gefettete Springform [cite: 69]"],
            [cite_start]"Anleitung": ["Alle Zutaten mischen [cite: 69][cite_start]", "In Form füllen [cite: 69][cite_start]", "Bei 175°C Umluft 60-70 Min. backen [cite: 70, 71][cite_start]", "Abkühlen lassen [cite: 72]"]
        },
        "American Cheeseburger": {
            [cite_start]"Zutaten": ["600 g Rinderhack", "Salz, Pfeffer", "4 Scheiben Schmelzkäse", "Essiggurken, Tomaten, Zwiebelringe, Eisbergsalat", "Senf, Ketchup", "4 Brötchen [cite: 86-89]"],
            [cite_start]"Werkzeuge": ["Holzkohlegrill oder Teflonpfanne [cite: 89, 95]"],
            [cite_start]"Anleitung": ["Patties formen und 2-3 Min. pro Seite grillen [cite: 91][cite_start]", "Käse darauf schmelzen lassen [cite: 92][cite_start]", "Brötchen toasten [cite: 92][cite_start]", "Belegen und mit Ketchup/Senf servieren [cite: 93, 94]"]
        },
        "American Spare Ribs": {
            [cite_start]"Zutaten": ["2 kg Schweinerippchen", "Marinade: Öl, Paprika, Knoblauch, Rosmarin, Sojasauce, Honig", "Sauce: Ketchup, Essig, Zucker, Cayennepfeffer, Salz [cite: 98-114]"],
            [cite_start]"Werkzeuge": ["Küchenpapier", "Pinsel", "Grill oder Backofen [cite: 106-108]"],
            [cite_start]"Anleitung": ["Rippchen trockentupfen und einschneiden [cite: 106][cite_start]", "Marinieren und über Nacht kühlen [cite: 107][cite_start]", "Bei 220°C garen [cite: 108][cite_start]", "Sauce dazu servieren [cite: 114]"]
        },
        "Quarkkuchen (altes Rezept)": {
            [cite_start]"Zutaten": ["Teig: 125g Mehl, Backpulver, 1.5 Eier, 60g Butter, 35g Zucker", "Belag: 1.5kg Quark, 45g Mehl, 125g Zucker, 2.5-6 Eier, 0.06l Milch, 65-180g Butter [cite: 125-139]"],
            [cite_start]"Werkzeuge": ["Schüssel", "Gefettete Springform [cite: 121, 123]"],
            [cite_start]"Anleitung": ["Mürbeteig kneten [cite: 121][cite_start]", "Belag mischen und Eischnee unterheben [cite: 122][cite_start]", "Teig in Form legen, Rand hochziehen [cite: 123]", "Bei 160°C (Umluft) ca. [cite_start]1 Std. backen [cite: 124]"]
        },
        "Rosinenkuchen": {
            [cite_start]"Zutaten": ["150 g Butter", "150 g Zucker", "3 Eier", "250 g Mehl", "50 g Speisestärke", "1 Prise Salz", "3 TL Backpulver", "5 EL Milch", "100 g Rosinen [cite: 182-190]"],
            [cite_start]"Werkzeuge": ["Schüssel", "Gefettete Kastenform [cite: 175, 177]"],
            [cite_start]"Anleitung": ["Butter schaumig rühren [cite: 175][cite_start]", "Zucker und Eier unterrühren [cite: 175][cite_start]", "Trockene Zutaten und Milch/Rosinen einrühren [cite: 176]", "Bei 180°C ca. [cite_start]30-40 Min. backen [cite: 178]"]
        },
        "Fluffige Pancakes": {
            [cite_start]"Zutaten": ["250 g Mehl", "48 g Zucker", "8 g Backpulver", "8 g Natron", "Prise Salz", "Butter (geschmolzen)", "4 Eier (getrennt)", "16 oz Buttermilch [cite: 197]"],
            [cite_start]"Werkzeuge": ["Schüssel", "Sieb", "Pfanne [cite: 197, 200]"],
            [cite_start]"Anleitung": ["Mehl, Zucker, Backpulver/Natron sieben [cite: 200, 202][cite_start]", "Eigelb-Butter-Mischung mit Eiweiß/Buttermilch vereinen [cite: 208][cite_start]", "Mehlmischung unterrühren, 10 Min. kühlen [cite: 209, 210][cite_start]", "In Pfanne backen bis Blasen entstehen, dann wenden [cite: 211-214]"]
        },
        "Tortenboden (Grundteig)": {
            "Zutaten": ["200 g Mehl", "3 TL Backpulver", "125 g Zucker", "3 Pkt. [cite_start]Vanillezucker", "Prise Salz", "4 EL Milch", "1 Ei", "75 g Butter [cite: 230-233]"],
            [cite_start]"Werkzeuge": ["Rührschüssel", "Handmixgerät", "Tortenbodenform [cite: 224, 227]"],
            [cite_start]"Anleitung": ["Alle Zutaten außer Butter verrühren [cite: 224][cite_start]", "Kalte Butter unterkneten [cite: 225][cite_start]", "In Form streichen [cite: 227][cite_start]", "Bei 200°C 10 Min. backen [cite: 228]"]
        },
        "Rosinenkekse (Vollkorn)": {
            [cite_start]"Zutaten": ["125 g Butter", "75 g Zuckerrohrgranulat", "2 Eigelb", "200 g Dinkelmehl", "Prise Salz", "Zitronenschale", "50 g Rosinen [cite: 257-263]"],
            [cite_start]"Werkzeuge": ["Schüssel", "Backblech", "Backpapier [cite: 245, 247]"],
            [cite_start]"Anleitung": ["Butter, Eigelb und Zucker schaumig rühren [cite: 245][cite_start]", "Mehl und Gewürze zugeben, Rosinen unterkneten [cite: 245, 246][cite_start]", "Rollen formen, Scheiben schneiden [cite: 246, 247][cite_start]", "Bei 180°C 12-15 Min. backen [cite: 248]"]
        },
        "Marmorkuchen": {
            [cite_start]"Zutaten": ["300 g Butter", "270 g Zucker", "Vanillezucker, Rum-Aroma, Salz", "5 Eier", "375 g Mehl", "12 g Backpulver", "6 EL Milch", "20 g Kakao [cite: 285-297]"],
            [cite_start]"Werkzeuge": ["Rührschüssel", "Marmorkuchenform", "Gabel [cite: 270, 273, 274]"],
            [cite_start]"Anleitung": ["Buttermasse rühren, Eier einzeln zugeben [cite: 270, 271][cite_start]", "Mehlmischung und Milch unterrühren [cite: 272][cite_start]", "2/3 Teig einfüllen, Rest mit Kakao/Milch färben [cite: 273][cite_start]", "Marmorieren und bei 190°C 60 Min. backen [cite: 274, 275]"]
        },
        "Spitzbubenkekse": {
            [cite_start]"Zutaten": ["300 g Mehl", "150 g Butter", "125 g Zucker", "1 Ei", "Marmelade", "Puderzucker [cite: 315-320]"],
            [cite_start]"Werkzeuge": ["Schüssel", "Frischhaltefolie", "Ausstechformen [cite: 322, 323]"],
            [cite_start]"Anleitung": ["Teig kneten und 30 Min. kühlen [cite: 322][cite_start]", "1 cm dick ausrollen, ausstechen [cite: 323][cite_start]", "Bei 180°C Umluft 20 Min. backen [cite: 323][cite_start]", "Mit Marmelade füllen und Puderzucker bestreuen [cite: 324]"]
        },
        "Hamburger (Großmenge)": {
            [cite_start]"Zutaten": ["3 kg Rinderhack", "30 Brötchen", "30 Scheiben Käse", "30 Blätter Salat", "7,5 Tomaten", "7,5 Zwiebeln", "Mayonnaise, Ketchup [cite: 349-357]"],
            [cite_start]"Werkzeuge": ["Pfanne [cite: 336, 338]"],
            [cite_start]"Anleitung": ["Flache Fladen formen und 5 Min. braten [cite: 336][cite_start]", "Käse darauf schmelzen [cite: 337][cite_start]", "Zwiebeln braten [cite: 338][cite_start]", "Brötchen mit Saucen bestreichen und belegen [cite: 339-341]"]
        },
        "Zitronenschnitten": {
            [cite_start]"Zutaten": ["Teig: 250g Butter, 250g Zucker, Eier, 250g Mehl", "Belag: 1kg Zitronen-Joghurt, Sahne, Gelatine, Götterspeise Zitrone [cite: 363-368]"],
            [cite_start]"Werkzeuge": ["Handrührgerät", "Backrahmen (30x40)", "Topf [cite: 372, 377, 392]"],
            [cite_start]"Anleitung": ["Rührteig backen (200°C, 25 Min) [cite: 372-380][cite_start]", "Joghurt-Sahne-Creme mit Gelatine herstellen [cite: 383-385][cite_start]", "Boden füllen und 2 Std. kühlen [cite: 389, 390][cite_start]", "Götterspeise und Zitronen obenauf schichten [cite: 392-397]"]
        },
        "Mandelkekse": {
            [cite_start]"Zutaten": ["300 g Mehl", "200 g Vollkornmehl", "2 TL Backpulver", "Bittermandelöl", "340 g Butter", "200 g Mandeln (gehackt)", "150 g Zucker [cite: 402]"],
            [cite_start]"Werkzeuge": ["Schüssel", "Löffel", "Backblech [cite: 403, 404]"],
            [cite_start]"Anleitung": ["Alle Zutaten verkneten [cite: 403][cite_start]", "Kleine Häufchen auf Blech setzen [cite: 404][cite_start]", "Bei 180°C goldgelb backen [cite: 404]"]
        },
        "Franks and Beans": {
            [cite_start]"Zutaten": ["8 Würstchen", "8 Brötchen", "Kidney Bohnen", "Weiße Bohnen", "Barbecue-Soße [cite: 407-411]"],
            [cite_start]"Werkzeuge": ["Topf [cite: 414]"],
            [cite_start]"Anleitung": ["Bohnen in Sauce erhitzen [cite: 414][cite_start]", "Würstchen erwärmen [cite: 414][cite_start]", "In Brötchen schichten [cite: 415]"]
        },
        "Pizza Dogs": {
            [cite_start]"Zutaten": ["4 Würstchen", "4 Brötchen", "Pizza-Soße", "Mozzarella [cite: 417-420]"],
            [cite_start]"Werkzeuge": ["Mikrowelle [cite: 422]"],
            [cite_start]"Anleitung": ["Wurst in Brötchen legen [cite: 422][cite_start]", "Mit Soße und Käse bedecken [cite: 422]", "30 Sek. [cite_start]Mikrowelle [cite: 422]"]
        },
        "German Hot Dogs": {
            [cite_start]"Zutaten": ["Würstchen", "Brötchen", "Senf", "Sauerkraut", "Essiggurken [cite: 431]"],
            [cite_start]"Werkzeuge": ["Topf [cite: 431]"],
            [cite_start]"Anleitung": ["Brötchen mit Senf bestreichen [cite: 431][cite_start]", "Wurst, Sauerkraut und Gurken darauf geben [cite: 431]"]
        },
        "Tortilla Hot Dogs": {
            [cite_start]"Zutaten": ["4 Würstchen", "4 Weizentortillas", "Salsa", "Eissalat [cite: 433-437]"],
            [cite_start]"Werkzeuge": ["Pfanne/Mikrowelle zum Erwärmen [cite: 437]"],
            [cite_start]"Anleitung": ["Tortillas erwärmen [cite: 437][cite_start]", "Mit Salsa bestreichen und Salat belegen [cite: 437][cite_start]", "Wurst einrollen [cite: 437]"]
        },
        "New York Hot Dogs": {
            [cite_start]"Zutaten": ["2 Zwiebeln", "125 ml Ketchup", "Essig, brauner Zucker", "Bockwürste", "Brötchen [cite: 439-445]"],
            [cite_start]"Werkzeuge": ["Topf [cite: 447]"],
            [cite_start]"Anleitung": ["Zwiebeln mit Saucenzutaten 15 Min. simmern [cite: 447][cite_start]", "Würstchen mit Sauce in Brötchen schichten [cite: 448]"]
        },
        "Chili Dogs": {
            [cite_start]"Zutaten": ["Chili con Carne", "4 Brötchen", "4 Würstchen", "Geriebener Käse [cite: 451-454]"],
            [cite_start]"Werkzeuge": ["Topf [cite: 456]"],
            [cite_start]"Anleitung": ["Brötchen und Würstchen erhitzen [cite: 456][cite_start]", "Chili über Wurst geben [cite: 456][cite_start]", "Mit Käse bestreuen [cite: 457]"]
        },
        "Corn Dogs": {
            [cite_start]"Zutaten": ["Mehl, Maismehl", "Zucker, Backpulver, Chilipulver", "2 Eier, Milch, Öl", "Würstchen [cite: 460-471]"],
            [cite_start]"Werkzeuge": ["Friteuse", "Schüssel", "Holzstäbe [cite: 473, 475]"],
            [cite_start]"Anleitung": ["Glatten Teig anrühren [cite: 474][cite_start]", "Würstchen auf Stäbe stecken, im Teig wenden [cite: 475][cite_start]", "3-5 Min. bei 180°C frittieren [cite: 475, 476]"]
        },
        "Hot Dog Relish (Selbstgemacht)": {
            [cite_start]"Zutaten": ["3 kg Paprika (rot/grün)", "1,5 kg Zwiebeln", "Weißweinessig", "Zucker, Senfkörner, Salz [cite: 479-485]"],
            [cite_start]"Werkzeuge": ["Küchenmaschine", "Topf", "Schraubgläser [cite: 487, 489, 490]"],
            [cite_start]"Anleitung": ["Gemüse fein hacken [cite: 487][cite_start]", "15 Min. in kochendem Wasser ziehen lassen, abgießen [cite: 488][cite_start]", "Mit restlichen Zutaten 10 Min. köcheln [cite: 489][cite_start]", "In Gläser füllen [cite: 490]"]
        },
        "Müslikekse": {
            [cite_start]"Zutaten": ["250 g Sonnenblumenkerne", "125 g Mandeln", "125 g Rohrzucker", "1 Ei", "30 g Kokosraspel [cite: 499-502]"],
            [cite_start]"Werkzeuge": ["Schüssel", "Zwei Löffel", "Backblech [cite: 510]"],
            [cite_start]"Anleitung": ["Zutaten verrühren [cite: 510][cite_start]", "Häufchen auf Blech setzen [cite: 510][cite_start]", "Bei 175°C 10-15 Min. backen [cite: 510]"]
        },
        "Ofenkartoffeln mit Cayennepfeffer": {
            [cite_start]"Zutaten": ["1 kg Kartoffeln", "Olivenöl", "Honig", "Cayennepfeffer/Tabasco", "Salz, Rosmarin [cite: 513-518]"],
            [cite_start]"Werkzeuge": ["Backblech", "Pinsel [cite: 520, 521]"],
            [cite_start]"Anleitung": ["Kartoffeln halbieren, Schnittfläche ölen [cite: 513, 520][cite_start]", "Schalen mit Honig-Chili-Mix bestreichen [cite: 521]", "Bei 220°C ca. [cite_start]40 Min. backen [cite: 522]"]
        },
        "Schwarz-Weiß-Gebäck": {
            [cite_start]"Zutaten": ["750 g Mehl", "200 g Puderzucker", "500 g Butter", "1 EL Kakao [cite: 524-528]"],
            [cite_start]"Werkzeuge": ["Schüssel", "Kühlschrank", "Backblech [cite: 532, 533, 535]"],
            [cite_start]"Anleitung": ["Teig herstellen, 1/3 mit Kakao färben [cite: 530, 531][cite_start]", "Rollen formen, kühlen [cite: 533][cite_start]", "In Zucker rollen, Scheiben schneiden [cite: 534, 535][cite_start]", "Bei 180°C 15-20 Min. backen [cite: 536, 537]"]
        },
        "Turbo Mandelkekse": {
            [cite_start]"Zutaten": ["150 g Mehl", "100 g Vollkornmehl", "Backpulver, Vanillezucker", "Bittermandelöl, Milch, Butter", "100 g Mandeln, Zucker [cite: 623-632]"],
            [cite_start]"Werkzeuge": ["Schüssel", "Löffel", "Backblech [cite: 615, 616]"],
            [cite_start]"Anleitung": ["Alle Zutaten verkneten [cite: 615][cite_start]", "Kleine Häufchen auf Blech setzen [cite: 615, 616][cite_start]", "Bei 180°C goldgelb backen [cite: 616]"]
        },
        "Lasagne al forno": {
            [cite_start]"Zutaten": ["500 g Hackfleisch", "Tomaten (geschält/Sauce)", "Zucchini, Knoblauch", "Mozzarella, Pecorino, Parmesan", "Lasagneblätter, Béchamelsauce [cite: 638-646]"],
            [cite_start]"Werkzeuge": ["Pfanne", "Auflaufform", "Reibe [cite: 647, 652, 654]"],
            [cite_start]"Anleitung": ["Sauce mit Hack und Gemüse 1 Std. köcheln [cite: 647-650][cite_start]", "In Form schichten (Sauce, Nudeln, Béchamel) [cite: 654][cite_start]", "Bei 200°C Umluft 20 Min. backen [cite: 655, 656]"]
        },
        "Muffin Grundrezept": {
            [cite_start]"Zutaten": ["250 g Mehl", "250 g Zucker", "1/4 l Schlagobers", "4 Eier", "Backpulver [cite: 666-670]"],
            [cite_start]"Werkzeuge": ["Schüssel", "Muffinformen [cite: 677, 682]"],
            [cite_start]"Anleitung": ["Zutaten verrühren [cite: 677, 678][cite_start]", "Optional Kakao/Schoko zugeben [cite: 680]", "Bei 180°C ca. [cite_start]20 Min. backen [cite: 681, 682]"]
        },
        "Rührkuchen": {
            [cite_start]"Zutaten": ["250 g Butter", "250 g Zucker", "Vanillezucker", "4 Eier", "250 g Mehl", "Backpulver [cite: 700]"],
            [cite_start]"Werkzeuge": ["Rührschüssel", "Gefettete Backform [cite: 701, 703]"],
            [cite_start]"Anleitung": ["Buttermasse schaumig rühren, Eier einzeln zugeben [cite: 701][cite_start]", "Mehl unterziehen [cite: 702]", "Bei 180°C ca. [cite_start]1 Std. backen [cite: 703]"]
        },
        "Puddingstreusel": {
            [cite_start]"Zutaten": ["Puddingpulver", "Streusel: 500g Mehl, 400g Zucker, 400g Butter", "Teig: Butter, Zucker, Eier, Mehl, Backpulver, Milch [cite: 739-750]"],
            [cite_start]"Werkzeuge": ["Topf", "Eckige Backform [cite: 752, 758]"],
            [cite_start]"Anleitung": ["Pudding kochen [cite: 752][cite_start]", "Rührteig 15 Min. vorbacken (180°C) [cite: 756, 758][cite_start]", "Pudding und Streusel darauf verteilen [cite: 759, 760][cite_start]", "Weitere 20 Min. backen [cite: 762]"]
        },
        "Omas Bohnensalat": {
            [cite_start]"Zutaten": ["2,5 kg Bohnen", "1,25 kg Kartoffeln", "250 g Speck", "Zwiebeln, Essig, Öl, Zucker [cite: 786-795]"],
            [cite_start]"Werkzeuge": ["Topf", "Salatschüssel", "Pfanne [cite: 769-771, 773]"],
            [cite_start]"Anleitung": ["Bohnen und Kartoffeln garen [cite: 769, 770][cite_start]", "Mit Dressing vermischen, 1 Std. ziehen lassen [cite: 771, 772][cite_start]", "Speck knusprig braten und unterheben [cite: 773]"]
        },
        "Tortenboden (Easy)": {
            [cite_start]"Zutaten": ["4 Eier", "5 EL Öl", "5 EL Zucker", "5 EL Mehl", "Vanillezucker", "Backpulver [cite: 801-806]"],
            [cite_start]"Werkzeuge": ["Rührschüssel", "Eingefettete Form [cite: 807]"],
            [cite_start]"Anleitung": ["Alle Zutaten verrühren [cite: 807][cite_start]", "In Form füllen [cite: 807][cite_start]", "Bei 200°C 10-12 Min. backen [cite: 808]"]
        },
        "Ullis Vollkornkekse": {
            [cite_start]"Zutaten": ["80 g Margarine", "80 g Zucker", "1 Ei", "250 g Vollkornmehl", "Backpulver [cite: 843-853]"],
            [cite_start]"Werkzeuge": ["Schüssel", "Nudelholz", "Ausstechformen [cite: 823, 824]"],
            [cite_start]"Anleitung": ["Zutaten verkneten, kühlen [cite: 823, 824][cite_start]", "Ausrollen und ausstechen [cite: 824]", "Bei 200°C ca. [cite_start]10 Min. backen [cite: 824][cite_start]", "Optional dekorieren [cite: 825, 826]"]
        },
        "Texas Jailhouse Chili": {
            [cite_start]"Zutaten": ["1,5 kg Rinderwürfel", "500 g Schweinehack", "500 g Chorizo", "Zwiebeln, Knoblauch, Chilis", "Tomatenmark/Dose", "Bier, Schokolade, Gewürze [cite: 866-887]"],
            [cite_start]"Werkzeuge": ["Großer Topf [cite: 888, 889]"],
            [cite_start]"Anleitung": ["Fleisch anbraten, mit Bier ablöschen [cite: 888, 889][cite_start]", "Alle Zutaten außer Bohnen 2 Std. köcheln [cite: 890][cite_start]", "Bohnen separat mit Speck zubereiten und dazureichen [cite: 891, 892]"]
        }
    }

st.set_page_config(page_title="Meine Rezepte", page_icon="🥘", layout="wide")
st.title("👨‍🍳 Mein digitales Kochbuch")

menu = st.sidebar.radio("Navigation", ["Alle Rezepte", "Rezept bearbeiten", "Neues Rezept hinzufügen"])

if menu == "Alle Rezepte":
    selection = st.selectbox("Rezept wählen:", sorted(list(st.session_state.recipes.keys())))
    r = st.session_state.recipes[selection]
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🛒 Zutaten")
        for z in r["Zutaten"]: st.write(f"- {z}")
    with col2:
        st.subheader("🛠 Hilfsmittel")
        for w in r["Werkzeuge"]: st.write(f"- {w}")
    
    st.subheader("👨‍🍳 Anleitung")
    for i, step in enumerate(r["Anleitung"], 1):
        st.write(f"**{i}.** {step}")

elif menu == "Rezept bearbeiten":
    st.info("Funktion in Arbeit: Hier kannst du Mengen anpassen.")

elif menu == "Neues Rezept hinzufügen":
    st.header("📝 Neues Rezept")
    new_name = st.text_input("Name")
    new_zutaten = st.text_area("Zutaten (eine pro Zeile)")
    if st.button("Speichern"):
        st.success(f"Rezept '{new_name}' wurde vorgemerkt!")
