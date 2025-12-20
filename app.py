import streamlit as st

# Datenbank-Initialisierung ohne störende Sonderzeichen
if 'recipes' not in st.session_state:
    st.session_state.recipes = {
        "1-2-3-Teig": {
            "Zutaten": ["200 g Butter", "1 Pck. Vanillezucker", "150 g Zucker", "1 Ei", "325 g Mehl", "100 g Speisestärke"],
            "Werkzeuge": ["Handrührgerät (Knethaken)", "Arbeitsplatte", "Nudelholz", "Ausstechformen", "Backblech"],
            "Anleitung": ["Zucker, Vanillezucker, Speisestärke und Mehl vermischen", "Butter und Ei hinzufügen", "Kurz verkneten, dann per Hand zu glattem Teig verarbeiten", "Ausrollen, ausstechen und bei 200 Grad ca. 12 Min. backen"]
        },
        "American Cheeseburger": {
            "Zutaten": ["600 g Rinderhack", "Salz & Pfeffer", "4 Scheiben Schmelzkäse", "Essiggurken", "Tomatenscheiben", "Zwiebelringe", "Eisbergsalat", "Senf & Ketchup", "4 Brötchen"],
            "Werkzeuge": ["Grill oder Teflonpfanne"],
            "Anleitung": ["Patties formen und pro Seite 2-3 Min. grillen", "Nach dem Wenden Käse darauf schmelzen", "Brötchen toasten", "Untere Hälfte mit Senf bestreichen, belegen, Ketchup auf den Deckel und zuklappen"]
        },
        "American Spare Ribs": {
            "Zutaten": ["2 kg Schweinerippchen", "1/8 l Öl", "4 EL Paprikapulver", "2 Knoblauchzehen (gehackt)", "1 TL Rosmarin", "8 EL Sojasauce", "4 EL Honig", "Salz & Pfeffer"],
            "Werkzeuge": ["Küchenpapier", "Pinsel", "Backofen oder Grill"],
            "Anleitung": ["Rippchen trocken tupfen, Haut einschneiden und pfeffern", "Marinade anrühren und Fleisch einstreichen", "Über Nacht kühlen", "Bei 220 Grad im Ofen oder auf dem Grill garen"]
        },
        "Amerikanischer Nudelsalat": {
            "Zutaten": ["1500 g Farfalle", "6 Gläser Spargel", "3 Dosen Erbsen", "6 Becher Creme fraiche", "Italienische Kräuter", "Gekörnte Brühe"],
            "Werkzeuge": ["Topf", "Schüssel"],
            "Anleitung": ["Nudeln kochen und abkühlen lassen", "Creme fraiche mit Wasser, Brühe und Kräutern einkochen", "Gemüse abtropfen und zum Salat geben", "Dressing unterrühren"]
        },
        "Caesar's Salad": {
            "Zutaten": ["1 Römersalat", "100 g Parmesan", "Toastbrot", "Knoblauch", "Olivenöl", "1 Glas Sardellen", "Balsamico", "Dijonsenf", "Worcestersauce", "1 Eigelb", "Zitronensaft"],
            "Werkzeuge": ["Pürierstab", "Pfanne", "Salatschüssel"],
            "Anleitung": ["Dressing-Zutaten pürieren und mit Öl aufgießen", "Salat klein schneiden und vermischen", "Croutons in Pfanne rösten", "Mit Parmesan und Croutons bestreuen"]
        },
        "Chili Dogs": {
            "Zutaten": ["4 Würstchen", "4 Brötchen", "8 EL Chili con Carne", "Geriebener Käse"],
            "Werkzeuge": ["Topf"],
            "Anleitung": ["Brötchen und Würstchen erhitzen", "Chili über die Wurst geben", "Mit Käse bestreuen"]
        },
        "Corn Dogs": {
            "Zutaten": ["1 Tasse Mehl", "1 Tasse Maismehl", "1 EL Zucker", "1/2 Pck Backpulver", "1 TL Salz", "1 TL Chilipulver", "2 Eier", "1 Tasse Milch", "1/4 Tasse Öl", "Würstchen"],
            "Werkzeuge": ["Friteuse", "Holzspieße", "Schüssel"],
            "Anleitung": ["Trockene und flüssige Zutaten getrennt mischen, dann vereinen", "Würstchen auf Spieße stecken", "Im Teig wenden und 3-5 Min goldbraun fritieren"]
        },
        "Drumsticks San Francisco Style": {
            "Zutaten": ["1,5 kg Hühnerbeine", "75 ml Sojasauce", "1 EL Reisessig", "2 EL Sherry", "Saft einer Orange", "Orangenschale", "1 EL brauner Zucker", "1 Sternanis", "1 EL Maisstärke", "50 ml Wasser", "1 EL Ingwer", "1/2 Knoblauchzehe", "Chilischoten"],
            "Werkzeuge": ["Topf", "Backblech", "Pinsel"],
            "Anleitung": ["Saucenzutaten (außer Stärke/Wasser/Ingwer) aufkochen", "Stärkemischung einrühren und 1 Min kochen", "Vom Herd nehmen, Ingwer/Knoblauch einrühren", "10-15 Min ziehen lassen", "Hähnchen mit Sauce bestreichen und bei 200 Grad 30-40 Min backen"]
        },
        "Eierkuchen": {
            "Zutaten": ["200 g Mehl", "5 Eier", "400 ml Milch", "Prise Salz", "25 g Zucker", "Butter"],
            "Werkzeuge": ["Schüssel", "Sieb", "Pfanne"],
            "Anleitung": ["Mehl sieben und mit Milch glatt rühren", "Eier, Salz und Zucker unterrühren", "Dünne Pfannkuchen in Butter ausbacken"]
        },
        "Fluffige Pancakes": {
            "Zutaten": ["250 g Mehl", "48 g Zucker", "8 g Backpulver", "8 g Natron", "Prise Salz", "Butter (geschmolzen)", "4 Eier (getrennt)", "16 oz Buttermilch"],
            "Werkzeuge": ["Zwei Schüsseln", "Pfanne"],
            "Anleitung": ["Trockene Zutaten sieben", "Eigelb, Butter, Buttermilch und schaumiges Eiweiß mischen", "Mehlmasse unterrühren", "In der Pfanne backen, bis Blasen entstehen, dann wenden"]
        },
        "Franks and Beans": {
            "Zutaten": ["8 Würstchen", "8 Brötchen", "Kidney Bohnen", "Weiße Bohnen", "Barbecue-Soße"],
            "Werkzeuge": ["Topf"],
            "Anleitung": ["Bohnen in Sauce erhitzen", "Würstchen erwärmen", "Alles im Brötchen schichten"]
        },
        "German Hot Dogs": {
            "Zutaten": ["Würstchen", "Brötchen", "Senf", "Sauerkraut", "Essiggurken"],
            "Werkzeuge": ["Topf"],
            "Anleitung": ["Brötchen mit Senf bestreichen", "Wurst, heißes Sauerkraut und Gurken auflegen"]
        },
        "Hamburger (Einfach)": {
            "Zutaten": ["Hackfleisch vom Rind", "Brötchen", "Käse", "Zwiebeln", "Tomaten", "Salat", "Ketchup & Mayonnaise"],
            "Werkzeuge": ["Pfanne"],
            "Anleitung": ["Hackfladen braten", "Käse darauf schmelzen", "Zwiebeln rösten", "Brötchen bestreichen und belegen"]
        },
        "Hot Dog Relish": {
            "Zutaten": ["1,5 kg roter Paprika", "1,5 kg grüner Paprika", "1,5 kg Zwiebeln", "4 Tassen Weißweinessig", "1/2 Tasse Zucker", "Senfkörner", "Salz"],
            "Werkzeuge": ["Küchenmaschine", "Topf", "Gläser"],
            "Anleitung": ["Gemüse fein hacken", "15 Min in kochendem Wasser ziehen lassen, abgießen", "Mit Essig/Zucker/Gewürzen 10 Min köcheln", "Heiß in Gläser füllen"]
        },
        "Lasagne al forno": {
            "Zutaten": ["500 g Hackfleisch", "Geschälte Tomaten", "Tomatensoße", "Zucchini", "Knoblauch", "Mozzarella", "Pecorino", "Parmesan", "Lasagneblätter", "Bechamelsauce"],
            "Werkzeuge": ["Pfanne", "Auflaufform"],
            "Anleitung": ["Sauce mit Fleisch und Gemüse 1 Std köcheln", "Schichtweise mit Nudeln und Bechamelsauce in Form füllen", "Mit Käse bestreuen", "Bei 200 Grad ca. 20 Min backen"]
        },
        "Mandelkekse": {
            "Zutaten": ["300 g Mehl", "200 g Vollkornmehl", "2 TL Backpulver", "Bittermandelöl", "Butter", "100 g gehackte Mandeln", "150 g Zucker"],
            "Werkzeuge": ["Schüssel", "Backblech"],
            "Anleitung": ["Alle Zutaten verkneten", "Kleine Häufchen auf Blech setzen", "Bei 180 Grad goldgelb backen"]
        },
        "Marmorkuchen": {
            "Zutaten": ["300 g Butter", "270 g Zucker", "Vanillezucker", "Rum-Aroma", "5 Eier", "375 g Mehl", "12 g Backpulver", "Milch", "20 g Kakao"],
            "Werkzeuge": ["Rührschüssel", "Backform"],
            "Anleitung": ["Rührteig herstellen", "2/3 hell in Form füllen", "Rest mit Kakao/Milch mischen und marmorieren", "Bei 190 Grad ca. 60 Min backen"]
        },
        "Muffin Grundrezept": {
            "Zutaten": ["250 g Mehl", "250 g Zucker", "1/4 l Sahne", "4 Eier", "1 Pck Backpulver"],
            "Werkzeuge": ["Schüssel", "Muffinform"],
            "Anleitung": ["Alle Zutaten mischen", "In Formen füllen", "Bei 180 Grad ca. 20 Min backen"]
        },
        "Müslikekse": {
            "Zutaten": ["250 g Sonnenblumenkerne", "125 g Mandelstifte", "125 g brauner Zucker", "1 Ei", "30 g Kokosraspel"],
            "Werkzeuge": ["Schüssel", "Backblech"],
            "Anleitung": ["Alles verrühren", "Häufchen auf Blech setzen", "Bei 175 Grad 10-15 Min backen"]
        },
        "New York Hot Dogs": {
            "Zutaten": ["Zwiebeln", "1/2 Tasse Ketchup", "Essig", "Brauner Zucker", "Würstchen", "Brötchen"],
            "Werkzeuge": ["Topf"],
            "Anleitung": ["Zwiebeln mit Sauce 15 Min simmern", "In Brötchen mit Wurst servieren"]
        },
        "Ofenkartoffeln mit Cayennepfeffer": {
            "Zutaten": ["1 kg Kartoffeln", "Olivenöl", "Honig", "Cayennepfeffer", "Salz", "Rosmarin"],
            "Werkzeuge": ["Backblech", "Pinsel"],
            "Anleitung": ["Kartoffeln halbieren, Schnittfläche ölen", "Schale mit Honig-Chili-Mix bestreichen", "Bei 220 Grad ca. 40 Min backen"]
        },
        "Omas Bohnensalat": {
            "Zutaten": ["2,5 kg Bohnen", "1,25 kg Kartoffeln", "250 g Speck", "Zwiebeln", "Essig & Öl"],
            "Werkzeuge": ["Topf", "Schüssel", "Pfanne"],
            "Anleitung": ["Bohnen und Kartoffeln kochen", "Mit Dressing mischen und ziehen lassen", "Knusprigen Speck unterheben"]
        },
        "Pizza Dogs": {
            "Zutaten": ["Würstchen", "Brötchen", "Pizzasoße", "Mozzarella"],
            "Werkzeuge": ["Mikrowelle"],
            "Anleitung": ["Wurst im Brötchen mit Sauce und Käse belegen", "30 Sek in Mikrowelle erhitzen"]
        },
        "Puddingstreusel": {
            "Zutaten": ["Puddingpulver Vanille", "Teig: 175g Butter, 180g Zucker, 4 Eier, 350g Mehl, Backpulver", "Streusel: 500g Mehl, 400g Zucker, 400g Butter"],
            "Werkzeuge": ["Topf", "Backform"],
            "Anleitung": ["Pudding kochen", "Teig 15 Min vorbacken (180 Grad)", "Pudding und Streusel darauf, weitere 20 Min backen"]
        },
        "Quarkkuchen (Alt)": {
            "Zutaten": ["Teig: 125g Mehl, Butter, Zucker, Ei", "Belag: 1,5 kg Quark, Zucker, Eier, Milch, Butter"],
            "Werkzeuge": ["Schüssel", "Springform"],
            "Anleitung": ["Mürbeteig herstellen", "Belag anrühren, Eischnee unterheben", "In Form füllen und bei 160 Grad ca. 1 Std backen"]
        },
        "Rosinenkekse": {
            "Zutaten": ["125 g Butter", "75 g Zuckerrohrgranulat", "2 Eigelb", "200 g Dinkelmehl", "Rosinen", "Zitronenschale"],
            "Werkzeuge": ["Schüssel", "Backblech"],
            "Anleitung": ["Teig kneten", "Rollen formen, Scheiben schneiden", "Bei 180 Grad 12-15 Min backen"]
        },
        "Rosinenkuchen": {
            "Zutaten": ["150 g Butter", "150 g Zucker", "3 Eier", "250 g Mehl", "5 TL Milch", "100 g Rosinen", "Backpulver"],
            "Werkzeuge": ["Schüssel", "Kastenform"],
            "Anleitung": ["Rührteig herstellen", "Rosinen unterrühren", "In Form füllen und bei 180 Grad 30-40 Min backen"]
        },
        "Rührkuchen": {
            "Zutaten": ["250 g Butter", "250 g Zucker", "4 Eier", "250 g Mehl", "Backpulver"],
            "Werkzeuge": ["Schüssel", "Kuchenform"],
            "Anleitung": ["Buttermasse schaumig schlagen, Eier einzeln unterrühren", "Mehl unterheben", "Bei 180 Grad ca. 1 Std backen"]
        },
        "Schneller Käsekuchen": {
            "Zutaten": ["1 kg Magerquark", "125 g Butter", "200 g Zucker", "4 Eier", "Grieß", "Vanillepuddingpulver"],
            "Werkzeuge": ["Schüssel", "Springform"],
            "Anleitung": ["Alle Zutaten mischen", "In Form füllen", "Bei 175 Grad ca. 60-70 Min backen"]
        },
        "Schwarz-Weiß-Gebäck": {
            "Zutaten": ["750 g Mehl", "200 g Puderzucker", "500 g Butter", "1 EL Kakao"],
            "Werkzeuge": ["Schüssel", "Folie"],
            "Anleitung": ["Teig kneten, 1/3 mit Kakao färben", "Kühlen, Muster formen", "Scheiben schneiden und bei 180 Grad 15-20 Min backen"]
        },
        "Schwarz-Weiß-Gebäck (Profi)": {
            "Zutaten": ["300 g Butter", "150 g Puderzucker", "400 g Mehl", "40 g Kakao", "1 Eigelb", "Vanille"],
            "Werkzeuge": ["Schüssel", "Lineal"],
            "Anleitung": ["Teig herstellen, hälftig färben", "In Streifen schneiden und schachbrettartig stapeln", "Mit Teigmantel umhüllen", "Scheiben schneiden und bei 180 Grad 12 Min backen"]
        },
        "Spitzbubenkekse": {
            "Zutaten": ["300 g Mehl", "150 g Butter", "125 g Zucker", "1 Ei", "Marmelade", "Puderzucker"],
            "Werkzeuge": ["Schüssel", "Ausstecher"],
            "Anleitung": ["Knetteig herstellen, kühlen", "Ringe ausstechen und backen", "Mit Marmelade zusammensetzen"]
        },
        "Texas Jailhouse Chili": {
            "Zutaten": ["1,5 kg Rinderwürfel", "500 g Schweinehack", "500 g Chorizo", "Bier", "Zartbitterschokolade", "Chilis", "Tomaten", "Bohnen (separat)"],
            "Werkzeuge": ["Großer Topf"],
            "Anleitung": ["Fleisch scharf anbraten", "Mit Bier ablöschen, Gewürze und Schokolade dazu", "2 Std köcheln lassen", "Bohnen separat mit Speck dazureichen"]
        },
        "Tortenboden (Easy)": {
            "Zutaten": ["4 Eier", "5 EL Öl", "5 EL Zucker", "5 EL Mehl", "Vanillezucker", "1 TL Backpulver"],
            "Werkzeuge": ["Schüssel", "Tortenbodenform"],
            "Anleitung": ["Alles verrühren", "In Form füllen", "Bei 200 Grad 10-12 Min backen"]
        },
        "Tortenboden (Grundrezept)": {
            "Zutaten": ["200 g Mehl", "3 TL Backpulver", "125 g Zucker", "Vanillezucker", "1 Ei", "75 g kalte Butter"],
            "Werkzeuge": ["Schüssel", "Form"],
            "Anleitung": ["Teig verrühren, kalte Butter unterkneten", "In Form streichen", "Bei 200 Grad 10 Min backen"]
        },
        "Tortilla Hot Dogs": {
            "Zutaten": ["4 Würstchen", "4 Tortillas", "Salsa", "Eisbergsalat"],
            "Werkzeuge": ["Pfanne"],
            "Anleitung": ["Tortillas erwärmen", "Mit Salsa und Salat belegen", "Wurst einrollen"]
        },
        "Ullis Vollkornkekse": {
            "Zutaten": ["80 g Margarine", "80 g Zucker", "1 Ei", "250 g Vollkornmehl", "Backpulver", "Sesam/Mohn/Nüsse"],
            "Werkzeuge": ["Schüssel", "Ausstecher"],
            "Anleitung": ["Teig kneten, ausrollen und ausstechen", "Bei 200 Grad 10 Min backen", "In Verzierung drücken"]
        },
        "Zitronenschnitten": {
            "Zutaten": ["250 g Butter", "250 g Zucker", "5 Eier", "250 g Mehl", "1 kg Zitronenjoghurt", "Gelatine", "Götterspeise Zitrone"],
            "Werkzeuge": ["Backblech", "Backrahmen"],
            "Anleitung": ["Rührteig backen", "Joghurtcreme mit Gelatine darauf verteilen", "Mit Götterspeise und Zitronenscheiben garnieren"]
        }
    }

st.set_page_config(page_title="Meine Rezepte", page_icon="🥘", layout="wide")
st.title("👨‍🍳 Mein digitales Kochbuch")

# Navigation
menu = st.sidebar.radio("Navigation", ["Alle Rezepte", "Neues Rezept hinzufügen"])

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

elif menu == "Neues Rezept hinzufügen":
    st.header("📝 Neues Rezept")
    st.write("Funktion wird im nächsten Schritt mit Datenbank-Anbindung aktiviert.")
