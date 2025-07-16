from mcp.server.fastmcp import FastMCP

mcp = FastMCP("rogerlin_google")

# 語言字串翻譯工具
@mcp.tool()
def translate_to_chinese(text: str) -> str:
    """將文字翻譯成中文"""

    # 預設prompt
    strDetails = f"翻譯輸出部分分為兩大類:\n\n"
    strDetails += f"1. 中文意義: 請幫我解釋一下這段話的意思，並用繁體中文解釋。如果遇到的是問句的話，也希望提供給我對應的該國語言回答參考。如果提供的範例句子是日文漢字也請一併提供給我平假名或片假名。另外如果是句子也幫我分析它的組成為何那樣寫。\n\n"
    strDetails += f"2. 舉一反三: 也把該單字或句子，以該語言的形式舉例生活化的簡易句子，好讓我學習該語言。 如果提供的範例句子是日文漢字也請一併提供給我平假名或片假名。希望範例盡可能是N4.N5的學生懂得文法。\n\n"
    strDetails += f"請根據以上要求，對「{text}」進行完整的翻譯和分析。\n\n"

    return f"需要翻譯的句子或單字: {text}\n\n" + strDetails

# 單字聯想工具
@mcp.tool()
def word_association(word: str) -> str:
    """聯想單字"""

    # 預設prompt
    strDetails = f"請根據以下要求，對「{word}」進行聯想:\n\n"
    strDetails += f"1. 請提供該單字的詞性、三句生活化例子。\n\n"
    strDetails += f"2. 請列出與該單字相關的同義詞、反義詞等等，有相關性的單字即可，我希望但單字是先顯示中文再顯示對應語言。\n\n"
    strDetails += f"3. 如果可以的話，2.顯示的單字也附上一句相關例句，越生活化越好。\n\n"
    strDetails += f"最後，以上內容都要顯示對應單字的語言，顯示對應的單字或句子文法，不用太難N4、N5程度即可。如果是日文漢字的話，要額外顯示平假名或片假名不然有些漢字不會念。\n\n"


    return f"需要聯想的單字: {word}\n\n" + strDetails

# 香水推薦
@mcp.tool()
def recommend_perfumes(country: str = "韓國、日本、台灣", age_group: str = "25-30") -> str:
    """香水推薦"""

    # 預設prompt
    strDetails = f"能不能幫我尋找{country}女性{age_group}歲之間喜歡男士用甚麼香水。\n\n"
    strDetails += f"近3年的統計，\n\n"
    strDetails += f"以國家為單位顯示top5，用表格(table)或markdown的樣貌，\n\n"
    strDetails += f"附上「香水名稱、台灣價格、台灣供貨狀況、味道描述、適合時段與場合、性別偏好、持香時間」。\n\n"
    strDetails += f"例如:\n\n"
    strDetails += f"香水名稱: Jo Malone 海鹽與鼠尾草\n\n"
    strDetails += f"台灣價格: 2699-2900元\n\n"
    strDetails += f"台灣供貨狀況: 大部分電商有貨，價格穩定，有折扣機會。\n\n"
    strDetails += f"味道描述: 清新海風與礦物鹽氣息，混搭地中海鼠尾草，略帶木質感。\n\n"
    strDetails += f"適合時段與場合: 白天／春夏，適合上班、日常、短約會。\n\n"
    strDetails += f"性別偏好: 中性偏女：女生喜歡、男生多接受。\n\n"
    strDetails += f"持香時間: 約 4–6 小時。\n\n"

    return strDetails

# 遊戲王牌組分析
@mcp.tool()
def analyze_yugioh_deck(deck: str) -> str:
    """分析遊戲王牌組"""

    # 預設prompt
    strDetails = f"請幫我分析這個遊戲王牌組主題為: {deck}\n\n"
    strDetails += f"希望你能根據牌組主題找到對應日文的部分，接下來會用到的任何卡片你都傳給我日文名稱即可。\n\n"
    strDetails += f"以下為我想快速得知的注意事項細節：\n\n"
    strDetails += f"1. 為快攻、控制、展開?\n\n"
    strDetails += f"2. 主要怕哪些手坑? (ex: マリス(malice)、オルフェゴール(orcust) 怕 聖遺物-聖槍)\n\n"
    strDetails += f"3. 該主題展開時要斷哪裡，並告訴我具體連鎖(chain)細節? (ex: V・HERO インクリース發效果時，這邊繳うらら是最傷的。)\n\n"
    strDetails += f"4. 先後手可能會放的坑?\n\n"
    strDetails += f"ps: 這邊這段最重要！！！我希望你給的卡片名稱是真的有存在，而不是你瞎掰的！！！！\n\n"

    return strDetails

# 日本語gogogo目錄聯想
@mcp.tool()
def japanese_gogogo_association(text: str, level: str = "N5") -> str:
    """聯想日本語gogogo目錄內容"""

    # 預設prompt
    strDetails = f"請根據日本語gogogo目錄內容「{text}」進行聯想，程度為:「{level}」\n\n"
    strDetails += f"會分成以下部分來教學:\n\n"
    strDetails += f"1. 單字: 為「{level}」會考的單字，並且用於文法教學時一併舉例使用。\n\n"
    strDetails += f"2. 文法: 一個章節大約有4個文法，所以你可以幫我聯想該內容會教哪些，並提供對應範例。\n\n"
    strDetails += f"3. 文法小老師: 這邊就是把前面文法的地方，用老師的口吻再簡單針對那些文法，講更細節的地方，好比為何這句子要用這個助詞之類的。\n\n"
    strDetails += f"又或是其他你覺得可以補充的文法細節。\n\n"
    strDetails += f"4. 補充: 這裡可以補充上述單字、文法，實際用於日本社會對答時的範例，ex: 大多時候跟熟人會說どっも，不會說ありがとうございます。太正式太教科書了，懂嗎類似這種例子。\n\n"
    strDetails += f"5. 最後: 因為我日文漢字沒有很好，希望有提到漢字時，能一併附上對應假名讓我知道怎麼念。\n\n"

    return f"需要聯想的單字: {text}\n\n" + strDetails

if __name__ == "__main__":
    mcp.run()