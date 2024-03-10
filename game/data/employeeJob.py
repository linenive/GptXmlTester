import enum

class Rank(enum.Enum):
    INTERN = 1
    STAFF = 2
    ASSISTANT_MANAGER = 3
    MANAGER = 4
    DEPUTY_GENERAL_MANAGER = 5
    GENERAL_MANAGER = 6
    EXECUTIVE = 7
    DIRECTOR = 8
    EXECUTIVE_MANAGER = 9
    VICE_PRESIDENT = 9
    PRESIDENT = 10

rank_names = {
    Rank.INTERN: "인턴",
    Rank.STAFF: "사원",
    Rank.ASSISTANT_MANAGER: "대리",
    Rank.MANAGER: "과장",
    Rank.DEPUTY_GENERAL_MANAGER: "차장",
    Rank.GENERAL_MANAGER: "부장",
    Rank.EXECUTIVE: "이사",
    Rank.DIRECTOR: "상무",
    Rank.EXECUTIVE_MANAGER: "전무",
    Rank.VICE_PRESIDENT: "부사장",
    Rank.PRESIDENT: "사장",
}

class JobGroup(enum.Enum):
    PROGRAMMING = 1
    ART = 2
    DESIGN = 3
    SOUND = 4
    SCENARIO = 5
    PM = 6
    SALES = 7
    MARKETING = 8
    HR = 9
    FINANCE = 10
    MANAGEMENT_SUPPORT = 11
    MANAGEMENT = 12
    OPERATION = 13
    SERVICE = 14
    SECURITY = 15
    RESEARCH = 16
    QA = 17

job_group_names = {
    JobGroup.PROGRAMMING: "프로그래밍",
    JobGroup.ART: "아트",
    JobGroup.DESIGN: "기획",
    JobGroup.SOUND: "사운드",
    JobGroup.SCENARIO: "시나리오",
    JobGroup.PM: "프로젝트 매니저",
    JobGroup.SALES: "영업",
    JobGroup.MARKETING: "마케팅",
    JobGroup.HR: "인사",
    JobGroup.FINANCE: "재무",
    JobGroup.MANAGEMENT_SUPPORT: "경영지원",
    JobGroup.MANAGEMENT: "경영",
    JobGroup.OPERATION: "운영",
    JobGroup.SERVICE: "서비스",
    JobGroup.SECURITY: "보안",
    JobGroup.RESEARCH: "연구",
    JobGroup.QA: "품질관리",
}
