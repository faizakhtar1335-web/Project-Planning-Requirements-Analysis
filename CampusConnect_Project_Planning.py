"""
CampusConnect - Project Planning & Requirements Analysis
Week 1 Internship Task

This Python file represents the project plan as structured data.
It can also print a concise project summary and requirements.
"""

PROJECT = {
    "name": "CampusConnect",
    "type": "Student Task & Event Management System",
    "target_users": ["Students", "Faculty/Coordinators"],
    "duration": "8 weeks",
}

OBJECTIVES = [
    "Manage academic and personal tasks.",
    "Track priorities, due dates, and completion status.",
    "Display important campus events.",
    "Provide secure authentication.",
    "Support testing, deployment, and maintenance.",
]

FUNCTIONAL_REQUIREMENTS = [
    "FR-01: User registration, login, and logout.",
    "FR-02: Create, edit, delete, and view tasks.",
    "FR-03: Task title, description, priority, due date, and status.",
    "FR-04: Filter and sort tasks.",
    "FR-05: View upcoming campus events.",
    "FR-06: Authorized coordinators manage events.",
    "FR-07: Dashboard shows pending tasks and upcoming events.",
    "FR-08: Validate required fields and show useful errors.",
]

NON_FUNCTIONAL_REQUIREMENTS = [
    "Usability",
    "Performance",
    "Security",
    "Reliability",
    "Maintainability",
    "Browser compatibility",
    "Scalability",
]

MILESTONES = [
    ("Week 1", "Planning & Requirements", "Requirements approved"),
    ("Week 2", "System Design", "Architecture and UI design reviewed"),
    ("Weeks 3-5", "Development", "Core features complete"),
    ("Week 6", "Testing", "Test baseline passed"),
    ("Week 7", "Deployment & Review", "Pilot release"),
    ("Week 8", "Final Documentation", "Project completed"),
]

RISKS = {
    "Changing requirements": "Use requirement approval and change tracking.",
    "Schedule delays": "Use milestones and prioritize core features.",
    "Security vulnerabilities": "Use secure authentication, validation, and access control.",
    "Data loss": "Use backups and recovery procedures.",
    "Low user adoption": "Conduct usability reviews and collect pilot feedback.",
}


def print_project_summary():
    print("=" * 60)
    print("CAMPUSCONNECT - PROJECT PLANNING SUMMARY")
    print("=" * 60)
    print(f"Project: {PROJECT['name']}")
    print(f"Type: {PROJECT['type']}")
    print(f"Target Users: {', '.join(PROJECT['target_users'])}")
    print(f"Duration: {PROJECT['duration']}")

    print("\nOBJECTIVES")
    for i, objective in enumerate(OBJECTIVES, 1):
        print(f"{i}. {objective}")

    print("\nFUNCTIONAL REQUIREMENTS")
    for requirement in FUNCTIONAL_REQUIREMENTS:
        print(f"- {requirement}")

    print("\nNON-FUNCTIONAL REQUIREMENTS")
    for requirement in NON_FUNCTIONAL_REQUIREMENTS:
        print(f"- {requirement}")

    print("\nTIMELINE & MILESTONES")
    for period, phase, milestone in MILESTONES:
        print(f"- {period}: {phase} -> {milestone}")

    print("\nRISK MITIGATION")
    for risk, mitigation in RISKS.items():
        print(f"- {risk}: {mitigation}")

    print("\nProject planning completed successfully.")


if __name__ == "__main__":
    print_project_summary()
