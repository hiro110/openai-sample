import openai
import os

openai.api_type = "azure"
openai.api_key = os.getenv("AOAI_APIKEY") 
openai.api_base = os.getenv("AOAI_APIBASE")
openai.api_version = "2023-03-15-preview"

# ユーザーからの質問
user_input = "仕事を効率的に進めるには時間管理と順位づけが大事だということを学びました。"
# user_input = "『××な睡眠法』では枕の選び方が取り上げられていますが、弊社の枕はオーダーメイドにもかかわらずお手頃価格です。是非URLをご参照ください。"
# user_input = "本書の編集者は結婚観に関する本を手がけておきながら、何度も結婚・離婚を繰り返していて信用ならない。"

# create a completion
# response = openai.ChatCompletion.create(
#   engine="gpt35-flier",
#   messages = [{"role":"system","content":"You are an AI assistant that helps people find information."},{"role":"user","content":f"以下のユーザ入力テキストに対して、以下の条件に該当する文字列があるかどうかを判断してください。\n該当する場合、該当する文字列を返してください。\n該当しない場合、「Not Exists!」と返してください。\nユーザ入力テキスト: {user_input}\n条件:\n1. 誹謗中傷\n2. 批判\n3. 要約や書籍に対して評点をつける行為\n4. 法令違反\n5. 犯罪行為\n6. 危険行為\n7. プライバシーの侵害"}],
#   temperature=0.7,
#   max_tokens=800,
#   top_p=0.95,
#   frequency_penalty=0,
#   presence_penalty=0,
#   stop=None)

response = openai.ChatCompletion.create(
  engine="gpt-4-32k-flier",
  messages = [
  {
    "role":"system",
    "content":"あなたはユーザ入力テキストの内容を精査するプロです。ユーザ入力テキストに対して、以下の条件に該当する文字列があるかどうかを判断してください。\n該当する場合、該当する文字列を返してください。\n該当しない場合、「None」と返してください。\n条件:\n1. 誹謗中傷\n2. 批判\n3. 要約や書籍に対して評点をつける行為\n4. 法令違反\n5. 犯罪行為\n6. 危険行為\n7. プライバシーの侵害\n8. 広告や宣伝・勧誘"
  },
  {
    "role":"user",
    "content":f"ユーザ入力テキスト: {user_input}\n"
  }],
  temperature=0,
  max_tokens=800,
  top_p=0.95,
  stop=None
)

# Parameter Detail
# prompt: inputするテキスト
# max_tokens: 生成する文章の最大単語数
# temperature:  0 - 2の範囲をとり、ランダム性を指定する。0であれば確定な文章を出力し、毎回同じ文章を生成
# top_p: temperatureと対となるもの。小さくすればするほど候補が確率の高いものに絞られるため、確定的になっていきます。
# stop: どんな単語が出現したら文章生成を打ち切るか？
# https://platform.openai.com/docs/api-reference/completions/create

print(response.choices[0].message.content.strip())
