from fpdf import FPDF
from fpdf.enums import XPos, YPos

# Menus
lunch_menu = {
    "Monday": ["Dal & Rice", "Bhindi Masala", "Roti / Raita", "Salad"],
    "Tuesday": ["Dal & Rice", "Mix Veg", "Roti / Raita", "Salad"],
    "Wednesday": ["Dal & Rice", "Paneer Bhurji", "Roti / Raita", "Mix Salad"],
    "Thursday": ["Dal & Rice", "Aalu Gobhi", "Roti / Raita", "Salad"],
    "Friday": ["Dal & Rice", "Chana Sabji", "Roti / Raita", "Salad"],
    "Saturday": ["Dal & Rice", "Matar Paneer", "Roti / Raita", "Salad"]
}

dinner_menu = {
    "Monday": ["Paneer Butter Masala", "Aloo Dry", "Rice / Roti", "Salad"],
    "Tuesday": ["Kadi Pakoda", "Cabbage Matar", "Rice / Roti", "Salad"],
    "Wednesday": ["Aloo Dum", "Dal Tadka", "Rice / Roti", "Salad"],
    "Thursday": ["Rajma Masala", "Gajar Matar", "Rice / Roti", "Salad"],
    "Friday": ["Aloo Paratha", "Green Chutney", "Curd"],
    "Saturday": ["Aloo Matar Sabji", "Kheer & Puri"]
}

# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", 'B', 16)
pdf.cell(0, 10, "Ghar Ka Khana - Homemade Meal Delivery Service", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
pdf.ln(8)

# Weekly Menu Table
pdf.set_font("Helvetica", 'B', 14)
pdf.cell(0, 10, "Weekly Menu (Monday to Saturday)", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(5)

# Table headers
pdf.set_font("Helvetica", 'B', 10)
day_width = 25
lunch_width = 85
dinner_width = 85

pdf.cell(day_width, 10, "Day", border=1, align="C")
pdf.cell(lunch_width, 10, "Lunch", border=1, align="C")
pdf.cell(dinner_width, 10, "Dinner", border=1, align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

# Table rows with fixed height
pdf.set_font("Helvetica", '', 8)
row_height = 20

for day in lunch_menu.keys():
    # Day column
    pdf.cell(day_width, row_height, day, border=1, align="C")
    
    # Lunch column - truncate text if too long
    lunch_text = ", ".join(lunch_menu[day])
    pdf.cell(lunch_width, row_height, lunch_text, border=1, align="L")
    
    # Dinner column - truncate text if too long
    dinner_text = ", ".join(dinner_menu[day])
    pdf.cell(dinner_width, row_height, dinner_text, border=1, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.ln(5)

# Delivery & Info
pdf.ln(8)
pdf.set_font("Helvetica", 'B', 14)
pdf.cell(0, 10, "Delivery Options & Services", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_font("Helvetica", '', 12)

info = [
    "- Delivery available to both Home & Office.",
    "- Want lunch at office and dinner at home? We've got you covered!",
    "- Choose between reusable tiffin service or disposable plate packing.",
    "- Meals are fresh, hygienic, and cooked with love.",
    "",
    "Contact us to subscribe to your weekly plan!",
    "Call/WhatsApp: +919608249514"
]

for line in info:
    if line.strip():  # Only process non-empty lines
        pdf.cell(0, 8, line, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    else:
        pdf.ln(4)  # Add spacing for empty lines

# Save it
pdf.output("Homemade_Meal_Menu.pdf")
