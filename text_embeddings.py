import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

print("Load dataset")
# load parsed dataset
df = pd.read_csv("C:\\Users\Egor\Projects\Ranking_vacancy\Ml_Hackaton_28-31\data\df_not_embedding.csv")

print("concatenation all texts for vacancy")
# concatenation all texts for vacancy
df["text_vacancy"] = df.apply(
    lambda x: (str(x["vacancy_name"]) + str(x["vacancy_description"]) + str(x["vacancy_comment"]))[:4000], axis=1)
df = df.drop(["vacancy_name", "vacancy_description", "vacancy_comment"], axis=1)

print("concatenation of all texts for resume")
# concatenation of all texts for resume
df["text_resume"] = df.apply(
    lambda x: (str(x["about"]) + str(x["key_skills"]) + str(x["work_position"]) + str(x["work_description"]))[:4000], axis=1
)
df = df.drop(["about", "key_skills", "work_position", "work_description"], axis=1)

print("save processed dataset")
df.to_csv("C:\\Users\Egor\Projects\Ranking_vacancy\Ml_Hackaton_28-31\data\df_for_embeddings.csv", index=False)

print("init bert model")
# init model based on bert
model = SentenceTransformer("cointegrated/rubert-tiny2")

# sentences to encoding for vacancies and resumes
vacancy_sentences = df["text_vacancy"].to_list()
resume_sentences = df["text_resume"].to_list()

print("get vacancy embeddings")
# get vacancy embeddings
vacancy_embeddings = model.encode(vacancy_sentences)
# save embeddings
vacancy_embeddings = pd.DataFrame(vacancy_embeddings, columns=["vac_emb_" + str(i) for i in range(len(vacancy_embeddings[0]))])
vacancy_embeddings.to_csv("C:\\Users\Egor\Projects\Ranking_vacancy\Ml_Hackaton_28-31\data\\vacancy_embeddings.csv", index=False)

# add embeddings to dataset
df = pd.concat([df, vacancy_embeddings], axis=1)
df.to_csv("C:\\Users\Egor\Projects\Ranking_vacancy\Ml_Hackaton_28-31\data\df_vacancy_embeddings.csv", index=False)


print("get resume embeddings")
# get resume embeddings
resume_embeddings = model.encode(resume_sentences)
resume_embeddings = pd.DataFrame(resume_embeddings, columns=["res_emb_" + str(i) for i in range(len(resume_embeddings[0]))])
#save embeddings
pd.DataFrame(resume_embeddings).to_csv("C:\\Users\Egor\Projects\Ranking_vacancy\Ml_Hackaton_28-31\data\\resume_embeddings.csv", index=False)

# add embeddings to dataset
df = pd.concat([df, pd.DataFrame(resume_embeddings)], axis=1)
df.to_csv("C:\\Users\Egor\Projects\Ranking_vacancy\Ml_Hackaton_28-31\data\df_all_embeddings.csv", index=False)
