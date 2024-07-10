import pandas as pd

if __name__ == "__main__":
    file_output = "../../../datasets/outputs/output.csv"

    # ler a coluna filePath do arquivo CSV e alterar de "../../../datasets/output/{file}" para "{file}"
    df = pd.read_csv(file_output)
    df['filePath'] = df['filePath'].apply(lambda x: x.split('/')[-1])
    df.to_csv(file_output, index=False)
