"""Module for generating PDF character sheets using reportlab."""
##AI generated code starts here with docstrings personally added
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from entities.skills import calculate_skill_value  # pylint: disable=import-error


class PDFGenerator:
    """Generates PDF character sheets for D&D 5e characters."""

    def __init__(self):
        """Initialize the PDF generator with default styles."""
        self.styles = getSampleStyleSheet()
        self.title_style = ParagraphStyle(
            "CustomTitle",
            parent=self.styles["Title"],
            fontSize=24,
            spaceAfter=20
        )
        self.heading_style = ParagraphStyle(
            "CustomHeading",
            parent=self.styles["Heading2"],
            fontSize=14,
            spaceAfter=10
        )

    def generate(self, character, filename):
        """Generate a PDF character sheet for the given character.

        Args:
            character: Character object to generate PDF for
            filename: Output filename for the PDF

        Returns:
            The filename where the PDF was saved
        """
        doc = SimpleDocTemplate(filename, pagesize=A4)
        elements = []
        elements += self._build_header(character)
        elements += self._build_stats(character)
        elements += self._build_skills(character)
        doc.build(elements)
        return filename

    def _build_header(self, character):
        """Build the header section of the PDF.

        Args:
            character: Character object

        Returns:
            List of PDF elements
        """
        elements = []
        elements.append(Paragraph(character.name, self.title_style))
        elements.append(Paragraph(
            f"Race: {character.race} | "
            f"Class: {character.character_class} | "
            f"Level: {character.level}",
            self.styles["Normal"]
        ))
        elements.append(Spacer(1, 0.5*cm))
        elements.append(Paragraph("Background", self.heading_style))
        elements.append(Paragraph(character.background, self.styles["Normal"]))
        elements.append(Spacer(1, 0.5*cm))
        return elements

    def _build_stats(self, character):
        """Build the ability scores section of the PDF.

        Args:
            character: Character object

        Returns:
            List of PDF elements
        """
        elements = []
        elements.append(Paragraph("Ability Scores", self.heading_style))
        stat_order = ["strength", "dexterity", "constitution",
                      "wisdom", "intelligence", "charisma"]
        stat_data = [["Ability", "Score", "Modifier"]]
        for stat in stat_order:
            value = character.stats[stat]
            modifier = character.get_modifier(stat)
            sign = "+" if modifier >= 0 else ""
            stat_data.append([stat.capitalize(), str(value), f"{sign}{modifier}"])

        stat_table = Table(stat_data, colWidths=[5*cm, 3*cm, 3*cm])
        stat_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ]))
        elements.append(stat_table)
        elements.append(Spacer(1, 0.5*cm))
        return elements

    def _build_skills(self, character):
        """Build the skill proficiencies section of the PDF.

        Args:
            character: Character object

        Returns:
            List of PDF elements
        """
        elements = []
        elements.append(Paragraph("Skill Proficiencies", self.heading_style))
        skill_data = [["Skill", "Value"]]
        for skill in sorted(character.skill_proficiencies):
            value = calculate_skill_value(
                skill, character.stats, character.skill_proficiencies
            )
            sign = "+" if value >= 0 else ""
            skill_data.append([
                skill.replace("_", " ").capitalize(),
                f"{sign}{value}"
            ])

        skill_table = Table(skill_data, colWidths=[7*cm, 3*cm])
        skill_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ]))
        elements.append(skill_table)
        return elements
##AI generated code ends here
