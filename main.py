meme_dict = {
                "SUS": "Singkatan dari suspicious, berarti mencurigakan",
    "FOMO": "Fear Of Missing Out, takut ketinggalan sesuatu",
    "GOAT": "Greatest Of All Time, yang terbaik sepanjang masa",
    "YEET": "Ekspresi untuk melempar sesuatu dengan kuat atau kegembiraan",
    "BOP": "Lagu yang sangat enak didengar",
    "VIBE": "Suasana atau perasaan yang dirasakan",
    "SLAPS": "Sesuatu yang sangat bagus atau keren, biasanya lagu",
    "NO CAP": "Tidak bohong atau serius",
    "STAN": "Penggemar berat atau mendukung seseorang secara fanatik",
    "SIMP": "Orang yang terlalu mengagumi atau memuja seseorang",
        "ZENNED OUT": "Santai dan tenang, bebas stres"
           }
for i in range(5):
    word = input("\nKetik kata brainrot yang ingin kamu ketahui").upper()
    if word in meme_dict.keys():
        print("\n", word, "adalah", meme_dict[word])
    else :
        print("\nApakah itu slang baru, artinya apa?")
