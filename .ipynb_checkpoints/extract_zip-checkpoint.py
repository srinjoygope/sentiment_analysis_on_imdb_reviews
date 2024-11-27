import zipfile

# Path to the zip file and extract destination
zip_file_path = 'imdb_reviews.zip'
extract_to = 'imdb_reviews/'

# Unzipping
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to)

print("Unzipping completed.")