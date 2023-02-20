# napisz skrypt pomagający oszacować ile godzin potrzeba na pobranie
# danych z sieci o rozmiarze 13 TB, jeżeli wiesz, że plik o rozmiarze 194 MB
# udało się pobrać w 5 sekund. wynik zaokrąglij do pełnych godzin

# 1 TB = 1024 GB = 1 048 576 MB
# 13 TB = 13 * 1 048 576 MB = 13 631 488 MB

oneTB_MB = 1_048_576
quality_TB = 13
download_size = quality_TB * oneTB_MB
File_download_speed = 194 / 5 # MB/s

print("Na pobranie 13 TB potrzeba niecałe", -round(-download_size / File_download_speed // 3600), "godzin.")
