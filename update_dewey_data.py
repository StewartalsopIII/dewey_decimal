import json

# Define the main class names
main_class_names = {
    "000": "Computer science, information & general works",
    "010": "Bibliographies",
    "020": "Library & information sciences",
    "030": "Encyclopedias & books of facts",
    "040": "Unassigned",
    "050": "Magazines, journals & serials",
    "060": "Associations, organizations & museums",
    "070": "News media, journalism & publishing",
    "080": "Quotations",
    "090": "Manuscripts & rare books",
    "100": "Philosophy & psychology",
    "110": "Metaphysics",
    "120": "Epistemology",
    "130": "Parapsychology & occultism",
    "140": "Specific philosophical schools",
    "150": "Psychology",
    "160": "Logic",
    "170": "Ethics",
    "180": "Ancient, medieval & Eastern philosophy",
    "190": "Modern Western philosophy",
    "200": "Religion",
    "210": "Philosophy & theory of religion",
    "220": "The Bible",
    "230": "Christianity & Christian theology",
    "240": "Christian moral & devotional theology",
    "250": "Christian orders & local church",
    "260": "Social & ecclesiastical theology",
    "270": "History of Christianity",
    "280": "Christian denominations",
    "290": "Other religions",
    "300": "Social sciences",
    "310": "Statistics",
    "320": "Political science",
    "330": "Economics",
    "340": "Law",
    "350": "Public administration & military science",
    "360": "Social problems & social services",
    "370": "Education",
    "380": "Commerce, communications & transportation",
    "390": "Customs, etiquette & folklore",
    "400": "Language",
    "410": "Linguistics",
    "420": "English & Old English languages",
    "430": "Germanic languages",
    "440": "Romance languages",
    "450": "Italian, Romanian & related languages",
    "460": "Spanish & Portuguese languages",
    "470": "Latin & Italic languages",
    "480": "Hellenic languages",
    "490": "Other languages",
    "500": "Science",
    "510": "Mathematics",
    "520": "Astronomy",
    "530": "Physics",
    "540": "Chemistry",
    "550": "Earth sciences & geology",
    "560": "Fossils & prehistoric life",
    "570": "Biology",
    "580": "Plants (Botany)",
    "590": "Animals (Zoology)",
    "600": "Technology",
    "610": "Medicine & health",
    "620": "Engineering & applied operations",
    "630": "Agriculture",
    "640": "Home & family management",
    "650": "Management & public relations",
    "660": "Chemical engineering",
    "670": "Manufacturing",
    "680": "Manufacture for specific uses",
    "690": "Building & construction",
    "700": "Arts & recreation",
    "710": "Civic & landscape art",
    "720": "Architecture",
    "730": "Sculpture, ceramics & metalwork",
    "740": "Drawing & decorative arts",
    "750": "Painting",
    "760": "Graphic arts",
    "770": "Photography, computer art, film, video",
    "780": "Music",
    "790": "Sports, games & entertainment",
    "800": "Literature",
    "810": "American literature in English",
    "820": "English & Old English literatures",
    "830": "Germanic literatures",
    "840": "Romance literatures",
    "850": "Italian, Romanian & related literatures",
    "860": "Spanish & Portuguese literatures",
    "870": "Latin & Italic literatures",
    "880": "Hellenic literatures",
    "890": "Literatures of other languages",
    "900": "History & geography",
    "910": "Geography & travel",
    "920": "Biography & genealogy",
    "930": "History of ancient world (to ca. 499)",
    "940": "History of Europe",
    "950": "History of Asia",
    "960": "History of Africa",
    "970": "History of North America",
    "980": "History of South America",
    "990": "History of other areas"
}

# Load the existing data
with open('dewey_data.py', 'r') as file:
    content = file.read()
    dewey_system = eval(content.split('=', 1)[1].strip())

# Update the data structure
updated_dewey_system = {}
for main_class, subdivisions in dewey_system.items():
    class_name = main_class_names.get(main_class, "Unknown")
    full_class_name = f"{main_class} - {class_name}"
    updated_dewey_system[full_class_name] = subdivisions

# Save the updated data
with open('updated_dewey_data.py', 'w') as file:
    file.write("dewey_system = ")
    json.dump(updated_dewey_system, file, indent=4)

print("Updated Dewey Decimal System data has been saved to 'updated_dewey_data.py'")