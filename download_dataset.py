from datasets import load_dataset

def download_and_save():
    # Memuat dataset
    ds = load_dataset("naver-clova-ix/cord-v2")

    # Menyimpan dataset di folder 'data'
    ds.save_to_disk("data")
    print("Dataset berhasil disimpan di folder 'data'.")

if __name__ == "__main__":
    download_and_save()