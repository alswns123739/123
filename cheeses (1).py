import random
import time
#112222
상점_상품 = []
상점_마지막갱신 = 0

스크롤_사용중 = {
    "active": False,
    "type": None  # "초급", "중급", "고급"
}


# 플레이어 기본 정보
player = {
    "name": "용사",
    "weapon_level": 0,

    "inventory": {
        "강화석": 100,
        "고급강화석": 0,
        "초월강화석": 0,
        "각성석": 0,
        "골드": 1000000,
        "초급스크롤": 0,
        "중급스크롤": 0,
        "고급스크롤": 0
    },

    "profile": {
        "레벨": 1,
        "경험치": 0,
        "클래스": "초보자"
    },

    "attack": 200,       # 기본 공격력
    "hp": 1000,
    "max_hp": 1000,
    "mp": 100,
    "max_mp": 100,

    "stage": 1,
    "sub_stage": 1
}


# 플레이어 정보 밑에 추가
player["attack"] = 200  # 기본 공격력

# 강화 확률 테이블
강화_확률 = {
    1: 100, 2: 95, 3: 90, 4: 85, 5: 80,
    6: 75, 7: 70, 8: 65, 9: 60, 10: 50,
    11: 50, 12: 40, 13: 30, 14: 20, 15: 10,
    16: 9, 17: 8, 18: 7, 19: 6, 20: 5
}

def 강화_스크롤_사용(번호):
    scroll_types = {1: "초급", 2: "중급", 3: "고급"}
    if 번호 not in scroll_types:
        print("잘못된 스크롤 번호입니다.")
        return

    종류 = scroll_types[번호]
    # 플레이어가 해당 스크롤을 가지고 있는지 체크
    key = f"{종류}스크롤"
    if player["inventory"].get(key, 0) <= 0:  # ✅ 올바른 방식

        print(f"{종류} 강화 스크롤이 없습니다.")
        return

    # 스크롤 사용 활성화
    스크롤_사용중["active"] = True
    스크롤_사용중["type"] = 종류
    player[key] -= 1
    print(f"{종류} 강화 스크롤을 사용했습니다. 다음 강화 시 100% 성공 확률입니다.")

def 체력바(현재, 최대, 길이=20):
    비율 = 현재 / 최대 if 최대 > 0 else 0
    채워짐 = int(비율 * 길이)
    bar = '█' * 채워짐 + '-' * (길이 - 채워짐)
    return f"[{bar}] {현재}/{최대}"


def 상점_상품_생성():
    상품_풀 = []

    # 강화석 (기본)
    상품_풀.append({"이름": "강화석 100개", "종류": "강화석", "수량": 100, "확률": 50})

    # 고급 강화석
    상품_풀.append({"이름": "고급 강화석 10개", "종류": "고급강화석", "수량": 10, "확률": 20})

    # 초월 강화석
    상품_풀.append({"이름": "초월 강화석 1개", "종류": "초월강화석", "수량": 1, "가격": {"골드": 1000000}, "확률": 5})

    # 각성석
    상품_풀.append({"이름": "각성석 1개", "종류": "각성석", "수량": 1, "가격": {"골드": 5000000}, "설명": "무기 최대강화 +1", "확률": 1})

    # 스크롤
    상품_풀 += [
        {"이름": "초급 강화 스크롤", "종류": "스크롤", "가격": {"골드": 50000}, "설명": "1~10강 100% 확정", "확률": 10},
        {"이름": "중급 강화 스크롤", "종류": "스크롤", "가격": {"골드": 500000, "강화석": 100}, "설명": "10~18강 100% 확정", "확률": 7},
        {"이름": "고급 강화 스크롤", "종류": "스크롤", "가격": {"골드": 3000000, "초월강화석": 5}, "설명": "19~22강 100% 확정", "확률": 2}
    ]

    return random.choices(상품_풀, weights=[i["확률"] for i in 상품_풀], k=3)


def 강화():
    level = player["weapon_level"]

    if level >= 20:
        print("20강을 달성했습니다! 이제 /초월강화소를 이용할 수 있습니다.")
        return

    print(f"\n[강화 시도] 현재 무기 강화 단계: +{level}")
    print(f"현재 공격력: {player['attack']}")

    종류 = None
    if 스크롤_사용중["active"]:
        종류 = 스크롤_사용중["type"]

    if level < 10:
        stone_cost = 10 * (2 ** level)
        gold_cost = 1000 * (3 ** level)
        success_rate = 강화_확률.get(level + 1, 0)

        if 종류 == "초급" and 1 <= level + 1 <= 10:
            success_rate = 100

        if player["inventory"]["강화석"] < stone_cost or player["inventory"]["골드"] < gold_cost:
            print(f"재료 부족! (필요 강화석: {stone_cost}, 필요 골드: {gold_cost})")
            return

        print(f"성공 확률: {success_rate}% | 강화석 필요: {stone_cost}개 | 골드 필요: {gold_cost}G")
        시도 = input("강화를 시도하시겠습니까? (y/n): ").lower()

        if 시도 == 'y':
            player["inventory"]["강화석"] -= stone_cost
            player["inventory"]["골드"] -= gold_cost
            print("강화 중...")
            time.sleep(1)  # 1초 대기
            if random.randint(1, 100) <= success_rate:
                player["weapon_level"] += 1
                print(f"강화 성공! 현재 +{player['weapon_level']}")

                if player["weapon_level"] <= 5:
                    atk = 200
                else:
                    atk = 300
                player["attack"] += atk
                player["max_hp"] += atk * 5
                print(f"공격력이 증가했습니다! 현재 공격력: {player['attack']}")
                print(f"최대 체력이 증가했습니다! 현재 최대 체력: {player['max_hp']}")


                스크롤_사용중["active"] = False
                스크롤_사용중["type"] = None
            else:
                print("강화 실패...")
                스크롤_사용중["active"] = False
                스크롤_사용중["type"] = None
        else:
            print("강화를 취소했습니다.")
            스크롤_사용중["active"] = False
            스크롤_사용중["type"] = None

    elif level < 20:
        stone_cost = 10
        gold_cost = 100000
        success_rate = 강화_확률.get(level + 1, 0)

        if 종류 == "중급" and 10 <= level + 1 <= 18:
            success_rate = 100
        elif 종류 == "고급" and 19 <= level + 1 <= 22:
            success_rate = 100

        if player["inventory"]["고급강화석"] < stone_cost or player["inventory"]["골드"] < gold_cost:
            print(f"재료 부족! (필요 고급 강화석: {stone_cost}, 필요 골드: {gold_cost}G)")
            return

        print(f"성공 확률: {success_rate}% | 고급 강화석 필요: {stone_cost}개 | 골드 필요: {gold_cost}G")
        시도 = input("강화를 시도하시겠습니까? (y/n): ").lower()

        if 시도 == 'y':
            player["inventory"]["고급강화석"] -= stone_cost
            player["inventory"]["골드"] -= gold_cost
            print("강화 중...")
            time.sleep(1)  # 1초 대기
            if random.randint(1, 100) <= success_rate:
                player["weapon_level"] += 1
                print(f"공격력이 증가했습니다! 현재 공격력: {player['attack']}")
                print(f"최대 체력이 증가했습니다! 현재 최대 체력: {player['max_hp']}")


                if player["weapon_level"] <= 15:
                    atk = 500
                else:
                    atk = 1000
                player["attack"] += atk
                player["max_hp"] += atk * 5

                print(f"공격력이 증가했습니다! 현재 공격력: {player['attack']}")
                print(f"최대 체력이 증가했습니다! 현재 최대 체력: {player['max_hp']}")

            else:
                print("강화 실패...")
        else:
            print("강화를 취소했습니다.")


def 생성_몬스터(stage, sub_stage):
    전체스테이지 = (stage - 1) * 10 + sub_stage
    is_boss = (sub_stage % 10 == 0)

    if stage == 10 and sub_stage == 10:
        return {"이름": "최종보스 10-10", "hp": 2_000_000, "공격력": 200_000, "is_boss": True}

    if not is_boss:
        hp = 500 + 전체스테이지 * 500
        공격력 = 150 + 전체스테이지 * 100
        이름 = f"몬스터 {stage}-{sub_stage}"
        return {"이름": 이름, "hp": hp, "공격력": 공격력, "is_boss": False}
    else:
        이전_스테이지 = 전체스테이지 - 1
        일반_hp = 500 + 이전_스테이지 * 500
        일반_공격력 = 150 + 이전_스테이지 * 100
        배수 = 10 + stage
        hp = 일반_hp * 배수
        공격력 = 일반_공격력 * 배수
        이름 = f"보스 {stage}-{sub_stage}"
        return {"이름": 이름, "hp": hp, "공격력": 공격력, "is_boss": True}


# 던전 함수
def 던전():
    stage = player["stage"]
    sub_stage = player["sub_stage"]
    monster = 생성_몬스터(stage, sub_stage)

    print(f"\n>> 던전 {stage}-{sub_stage} 입장!")
    print(f"적 등장: {monster['이름']} | HP: {monster['hp']} | 공격력: {monster['공격력']}\n")

    보스_턴_카운트 = 0
    화염_장막_유효_턴 = 0
    스킬_리스트 = [1, 2, 3, 4, 5, 6]
    monster_max_hp = monster["hp"]

    while monster["hp"] > 0 and player["hp"] > 0:
        print(f"\n==================== 턴 {보스_턴_카운트 + 1} ====================")

        # 🧠 보스 선공 AI
        if monster["is_boss"]:
            보스_턴_카운트 += 1
            if 보스_턴_카운트 <= 6:
                스킬번호 = 스킬_리스트[보스_턴_카운트 - 1]
            else:
                스킬번호 = random.choice(스킬_리스트)

            print(f"\n>> [보스 선공] 스킬 {스킬번호} 사용!")

            if 스킬번호 in [1, 5]:  # 화염의 장막
                화염_장막_유효_턴 = 2
                print("🔥 화염의 장막 발동! 2턴간 공격이 반사됩니다!")
            elif 스킬번호 in [2, 3, 4]:
                피해 = int(monster["공격력"] * 2.5)
                player["hp"] -= 피해
                print(f"🔫 강화 피스톨! {피해}의 피해를 입었습니다.")
            elif 스킬번호 == 6:
                피해 = int(player["hp"] * 0.3)
                player["hp"] -= 피해
                print(f"☣ 감염! 현재 체력의 30%({피해}) 피해를 입었습니다.")

            if player["hp"] <= 0:
                break

        # 플레이어 상태 표시
        print(f"[내 턴] 체력: {player['hp']} / {player['max_hp']} | 마나: {player['mp']}/{player['max_mp']}")
        print(f"{monster['이름']} HP: {체력바(monster['hp'], monster_max_hp, 30)}")

        명령어 = input("행동 선택 (/공격 /방어 /스킬): ").lower()

        if 명령어 == "/공격":
            damage = player["attack"]
            if 화염_장막_유효_턴 > 0:
                player["hp"] -= damage
                print(f"⚠️ 화염의 장막 반사! 당신은 {damage} 피해를 입었습니다!")
            else:
                monster["hp"] -= damage
                print(f">> {monster['이름']}에게 {damage} 데미지를 입혔습니다.")
        elif 명령어 == "/방어":
            print(">> 방어 기능은 아직 구현되지 않았습니다.")
            continue
        elif 명령어 == "/스킬":
            print(">> 스킬 기능은 아직 구현되지 않았습니다.")
            continue
        else:
            print(">> 잘못된 명령입니다.")
            continue

        # 일반 몬스터 반격 (보스는 이미 선공했으므로 무시)
        if monster["hp"] > 0 and not monster["is_boss"]:
            time.sleep(0.8)
            피해 = monster["공격력"]
            player["hp"] -= 피해
            print(f">> {monster['이름']}의 반격! {피해} 피해를 입었습니다.")

        # 화염 장막 효과 감소
        if 화염_장막_유효_턴 > 0:
            화염_장막_유효_턴 -= 1


    if player["hp"] <= 0:
        print("\n>> 당신은 쓰러졌습니다... 게임 오버 (혹은 마을로 귀환).")
        player["hp"] = player["max_hp"]
        return
    else:
            
        print(f"\n>> {monster['이름']} 처치 완료!")

        전체스테이지 = (stage - 1) * 10 + sub_stage

        if monster["is_boss"]:
            if stage == 10 and sub_stage == 10:
                보상 = 2_500_000  # 최종보스 고정 보상
            else:
                일반_보상 = 1000 + 전체스테이지 * 500
                보상 = 일반_보상 * 10
        else:
            보상 = 1000 + 전체스테이지 * 500

                # ✅ 보스 확률 드랍
        if monster["is_boss"]:
            전체스테이지 = (stage - 1) * 10 + sub_stage
            드랍표 = [
                ("강화석", 50, 100),
                ("고급강화석", min(35 + 전체스테이지 * 0.1, 100), 10),
                ("초월강화석", min(10 + 전체스테이지 * 0.05, 100), 1),
                ("초급스크롤", min(2 + 전체스테이지 * 0.05, 100), 1),
                ("중급스크롤", min(2 + 전체스테이지 * 0.05, 100), 1),
                ("고급스크롤", min(1 + 전체스테이지 * 0.05, 100), 1),
                ("각성석", min(1 + 전체스테이지 * 0.05, 100), 1)
            ]

            드랍굴림 = random.uniform(0, 100)
            누적 = 0
            for 아이템, 확률, 기본수량 in 드랍표:
                누적 += 확률
                if 드랍굴림 <= 누적:
                    보정수량 = 기본수량 + 전체스테이지 // 20
                    player["inventory"][아이템] = player["inventory"].get(아이템, 0) + 보정수량
                    print(f"🎁 드랍 아이템 획득! {아이템} {보정수량}개")
                    break


        if sub_stage < 10:
            player["sub_stage"] += 1
        else:
            if stage == 10:
                print(">> 최종보스를 처치했습니다! 던전 클리어!!")
            else:
                player["stage"] += 1
                player["sub_stage"] = 1
                print(f">> 던전 {stage + 1}이 열렸습니다!")

        player["hp"] = player["max_hp"]
        player["mp"] = player["max_mp"]





        if sub_stage < 10:
            player["sub_stage"] += 1
        else:
            if stage == 10:
                print(">> 최종보스를 처치했습니다! 던전 클리어!!")
            else:
                player["stage"] += 1
                player["sub_stage"] = 1
                print(f">> 던전 {stage + 1}이 열렸습니다!")

        player["hp"] = player["max_hp"]
        player["mp"] = player["max_mp"]



# 프로필 출력
def 프로필():
    print("\n[프로필 정보]")
    for key, value in player["profile"].items():
        print(f"{key}: {value}")
    print(f"무기 강화 단계: +{player['weapon_level']}")
    print(f"보유 골드: {player['inventory']['골드']}")
    print(f"강화석: {player['inventory']['강화석']}\n")

# 인벤토리 출력
def 인벤토리():
    print("\n[🎒 인벤토리 목록]")

    # 현재 구현된 아이템 목록
    아이템_리스트 = [
        "강화석", "고급강화석", "초월강화석", "각성석", "골드",
        "초급스크롤", "중급스크롤", "고급스크롤"
    ]

    출력된_항목 = False
    for 아이템 in 아이템_리스트:
        수량 = player["inventory"].get(아이템, 0)
        if 수량 > 0:
            print(f"{아이템}: {수량}")
            출력된_항목 = True

    if not 출력된_항목:
        print("보유 중인 아이템이 없습니다.")

def 상점():
    global 상점_상품, 상점_마지막갱신

    now = time.time()
    if now - 상점_마지막갱신 >= 300 or not 상점_상품:
        상점_상품 = 상점_상품_생성()
        상점_마지막갱신 = now
        print("\n[상점이 갱신되었습니다!]")

    print("\n[🛒 상점 목록]")
    for idx, item in enumerate(상점_상품, 1):
        if item["종류"] == "강화석":
            할인율 = min(30, int((item["수량"] / 1000) * 10))  # 10배 단위마다 10% 할인
            단가 = 100 * (1 - 할인율 / 100)
            총가격 = int(단가 * item["수량"])
            item["가격"] = {"골드": 총가격}
        elif item.get("가격") is None:
            item["가격"] = {"골드": item["수량"] * 10000}

        가격표시 = " / ".join(f"{v} {k}" for k, v in item["가격"].items())
        설명 = f" - {item['설명']}" if "설명" in item else ""
        print(f"{idx}. {item['이름']} - 가격: {가격표시}{설명}")

    선택 = input("구매할 아이템 번호 입력 (취소: Enter): ")
    if not 선택.isdigit():
        print("상점을 나갔습니다.")
        return

    idx = int(선택) - 1
    if idx < 0 or idx >= len(상점_상품):
        print("잘못된 선택입니다.")
        return

    아이템 = 상점_상품[idx]
    가격정보 = 아이템["가격"]

    # 재화 확인
    for 재화, 수량 in 가격정보.items():
        if player["inventory"].get(재화, 0) < 수량:
            print(f"구매 실패: {재화}가 부족합니다.")
            return

    # 재화 차감
    for 재화, 수량 in 가격정보.items():
        player["inventory"][재화] -= 수량

    # 아이템 지급
    종류 = 아이템["종류"]
    if 종류 in ["강화석", "고급강화석", "초월강화석", "각성석"]:
        player["inventory"].setdefault(종류, 0)
        player["inventory"][종류] += 아이템["수량"]
        print(f"{아이템['이름']} 구매 완료!")
    elif 종류 == "스크롤":
        종류명 = 아이템["이름"].split()[0]  # 예: 초급
        key = f"{종류명}스크롤"
  # 예: "초급 스크롤" → "초급스크롤"
        player[key] = player.get(key, 0) + 1
        print(f"{아이템['이름']} 구매 완료! 인벤토리에 추가되었습니다.")

    else:
        print("알 수 없는 아이템입니다.")


# 명령어 입력 루프
def 메인루프():
    print("=== 텍스트 RPG 시작 ===")
    while True:
        명령어 = input("명령어를 입력하세요 (/강화 /던전 /프로필 /인벤토리 /상점 /종료): ")
        if 명령어 == "/강화":
            강화()
        elif 명령어 == "/던전":
            던전()
        elif 명령어 == "/프로필":
            프로필()
        elif 명령어 == "/인벤토리":
            인벤토리()
        elif 명령어 == "/상점":
            상점()
        elif 명령어 == "/종료":
            print("게임을 종료합니다.")
            break
        elif 명령어.startswith("/강화 스크롤"):
            try:
                번호 = int(명령어.replace("/강화 스크롤", "").strip())
                강화_스크롤_사용(번호)
            except:
                print("명령어 형식: /강화 스크롤 1 또는 2 또는 3")


        else:
            print("알 수 없는 명령어입니다.")

# 게임 시작
메인루프()
