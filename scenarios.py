# scenarios.py

BUSINESS_SCENARIOS = [
    {
        "id": "q3_exec_summary",
        "title": "Q3 Sales Executive Summary",
        "role": "Product Manager",
        "task": "Summarize a 10-page Q3 regional sales report for the CEO.",
        "difficulty": "Beginner",
        "hint": "Assign a persona (Character), request 3 bullet points (Type), and set a 150-word cap (Extras).",
    },
    {
        "id": "hr_policy_update",
        "title": "Remote Work Policy Email",
        "role": "HR Director",
        "task": "Draft a company-wide email announcing a new hybrid work policy.",
        "difficulty": "Intermediate",
        "hint": "Set a supportive tone (Adjustments) and provide a sample opening line (Examples).",
    },
    {
        "id": "leadership_meeting_agenda",
        "title": "Oncology Leadership Meeting Agenda",
        "role": "Executive Assistant to the VP of Oncology Development",
        "task": "Create a 60-minute agenda for the monthly oncology development leadership meeting covering pipeline updates, budget review, and hiring.",
        "difficulty": "Beginner",
        "hint": "Ask for a table with time blocks and owners (Type of output) and cap each item at 15 minutes (Extras)."
    },
    {
        "id": "advisory_board_logistics",
        "title": "Advisory Board Travel Email",
        "role": "Administrative Coordinator, Oncology Medical Affairs",
        "task": "Draft an email to external advisory board members confirming meeting date, hotel, and travel reimbursement steps.",
        "difficulty": "Beginner",
        "hint": "Give it a professional, welcoming tone (Adjustments) and require a bulleted checklist of next steps (Type of output)."
    },
    {
        "id": "meeting_notes_summary",
        "title": "Study Team Meeting Summary",
        "role": "Administrative Assistant to a Clinical Development Team",
        "task": "Turn raw meeting notes from a study team sync into a summary with decisions, action items, owners, and due dates.",
        "difficulty": "Intermediate",
        "hint": "Paste a sample action item format to copy (Examples) and tell it not to invent owners or dates that aren't in the notes (Extras)."
    },
    {
        "id": "conference_abstract_tracker",
        "title": "Conference Abstract Deadline Tracker",
        "role": "Operations Coordinator, Oncology Research",
        "task": "Build a tracker of upcoming oncology conference abstract deadlines (e.g., ASCO, ESMO, ASH) with submission owners and internal review dates.",
        "difficulty": "Intermediate",
        "hint": "Specify the exact column headers you want (Type of output) and ask it to flag any dates it isn't certain about so you can verify them (Extras)."
    },
    {
        "id": "new_hire_onboarding",
        "title": "New Team Member Welcome Plan",
        "role": "Administrative Lead, Oncology Strategy Group",
        "task": "Create a first-week onboarding plan and welcome email for a new analyst joining the oncology strategy team.",
        "difficulty": "Intermediate",
        "hint": "Have it act as an experienced onboarding coordinator (Character) and match a friendly-but-polished house style (Adjustments)."
    },
    {
        "id": "exec_status_update",
        "title": "Pipeline Status Update for Executives",
        "role": "Chief of Staff, Oncology Portfolio Management",
        "task": "Condense five project status reports into a one-page executive update highlighting risks, milestones, and decisions needed.",
        "difficulty": "Advanced",
        "hint": "Provide one well-written status bullet as a model (Examples), limit it to 250 words (Extras), and ask for red/yellow/green labels (Type of output)."
    },
    {
        "id": "vendor_contract_comparison",
        "title": "CRO Vendor Comparison",
        "role": "Business Operations Coordinator, Oncology Development",
        "task": "Compare three contract research organization (CRO) proposals on cost, timeline, and service scope to prepare a recommendation for leadership.",
        "difficulty": "Advanced",
        "hint": "Request a side-by-side comparison table (Type of output), keep the tone neutral and objective (Adjustments), and remind it to use only the proposals you provide (Extras)."
    },
    {
        "id": "confidential_info_reminder",
        "title": "Data Handling Reminder Memo",
        "role": "Senior Administrative Assistant, Oncology Research Operations",
        "task": "Draft a short reminder memo to the team on handling confidential compound data and internal-only documents when using AI tools.",
        "difficulty": "Advanced",
        "hint": "Have it write as a compliance-minded communications lead (Character), keep it under 200 words with a do/don't list (Type of output), and avoid a scolding tone (Adjustments)."
    }
]


