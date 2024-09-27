{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyP4khbGUnCF2MlBTEqS8uAe"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","source":["def welcome_message():\n","    print(\"Selamat datang di Tes Pemahaman Python!\")\n","    print(\"Program ini akan menguji pemahaman dasar Anda tentang Python.\")\n","    print(\"Jawab setiap pertanyaan dengan benar untuk melanjutkan.\")\n","    print(\"Anda akan menerima umpan balik untuk setiap jawaban.\")\n","    print(\"Selamat mengerjakan!\\n\")\n","\n","\n","def ask_question(question, options, correct_option):\n","    print(question)\n","    for i, option in enumerate(options, 1):\n","        print(f\"{i}. {option}\")\n","\n","    while True:\n","        try:\n","            answer = int(input(\"Jawaban Anda (masukkan nomor): \"))\n","            if answer == correct_option:\n","                print(\"Benar!\\n\")\n","                return True\n","            else:\n","                print(\n","                    \"Salah. Jawaban yang benar adalah:\",\n","                    options[correct_option - 1],\n","                    \"\\n\",\n","                )\n","                return False\n","        except ValueError:\n","            print(\"Masukkan nomor yang valid.\\n\")\n","\n","\n","def quiz():\n","    score = 0\n","    total_questions = 5\n","\n","    # Pertanyaan 1\n","    question1 = \"Apa tipe data yang digunakan untuk menyimpan teks di Python?\"\n","    options1 = [\"int\", \"str\", \"list\", \"bool\"]\n","    correct_option1 = 2\n","    if ask_question(question1, options1, correct_option1):\n","        score += 1\n","\n","    # Pertanyaan 2\n","    question2 = (\n","        \"Struktur data mana yang digunakan untuk menyimpan pasangan kunci-nilai?\"\n","    )\n","    options2 = [\"List\", \"Tuple\", \"Dictionary\", \"Set\"]\n","    correct_option2 = 3\n","    if ask_question(question2, options2, correct_option2):\n","        score += 1\n","\n","    # Pertanyaan 3\n","    question3 = \"Apa hasil dari kode berikut: 3 + 5 * 2 ?\"\n","    options3 = [\"16\", \"13\", \"10\", \"11\"]\n","    correct_option3 = 2\n","    if ask_question(question3, options3, correct_option3):\n","        score += 1\n","\n","    # Pertanyaan 4\n","    question4 = \"Fungsi mana yang digunakan untuk menambahkan elemen ke list di Python?\"\n","    options4 = [\"insert()\", \"append()\", \"extend()\", \"add()\"]\n","    correct_option4 = 2\n","    if ask_question(question4, options4, correct_option4):\n","        score += 1\n","\n","    # Pertanyaan 5\n","    question5 = \"Apa yang dilakukan oleh pernyataan berikut: for i in range(5):\"\n","    options5 = [\n","        \"Mengulang dari 0 hingga 5 termasuk\",\n","        \"Mengulang dari 1 hingga 5 termasuk\",\n","        \"Mengulang dari 0 hingga 4\",\n","        \"Mengulang dari 1 hingga 4\",\n","    ]\n","    correct_option5 = 3\n","    if ask_question(question5, options5, correct_option5):\n","        score += 1\n","\n","    # Tampilkan hasil akhir\n","    print(f\"Tes Selesai! Skor Anda: {score} dari {total_questions}\")\n","    if score == total_questions:\n","        print(\"Luar biasa! Anda memahami dasar Python dengan sangat baik.\")\n","    elif score >= 3:\n","        print(\"Bagus! Anda memiliki pemahaman yang cukup kuat tentang Python.\")\n","    else:\n","        print(\"Anda perlu belajar lebih banyak. Cobalah lagi!\")\n","\n","\n","welcome_message()\n","quiz()"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"Hu6brE8flu4D","executionInfo":{"status":"ok","timestamp":1727408857570,"user_tz":-420,"elapsed":22370,"user":{"displayName":"reyhan satria","userId":"05657210630279970985"}},"outputId":"41c0c4fc-36d3-4847-d547-22f7d223b929"},"execution_count":3,"outputs":[{"output_type":"stream","name":"stdout","text":["Selamat datang di Tes Pemahaman Python!\n","Program ini akan menguji pemahaman dasar Anda tentang Python.\n","Jawab setiap pertanyaan dengan benar untuk melanjutkan.\n","Anda akan menerima umpan balik untuk setiap jawaban.\n","Selamat mengerjakan!\n","\n","Apa tipe data yang digunakan untuk menyimpan teks di Python?\n","1. int\n","2. str\n","3. list\n","4. bool\n","Jawaban Anda (masukkan nomor): 2\n","Benar!\n","\n","Struktur data mana yang digunakan untuk menyimpan pasangan kunci-nilai?\n","1. List\n","2. Tuple\n","3. Dictionary\n","4. Set\n","Jawaban Anda (masukkan nomor): 3\n","Benar!\n","\n","Apa hasil dari kode berikut: 3 + 5 * 2 ?\n","1. 16\n","2. 13\n","3. 10\n","4. 11\n","Jawaban Anda (masukkan nomor): 2\n","Benar!\n","\n","Fungsi mana yang digunakan untuk menambahkan elemen ke list di Python?\n","1. insert()\n","2. append()\n","3. extend()\n","4. add()\n","Jawaban Anda (masukkan nomor): 2\n","Benar!\n","\n","Apa yang dilakukan oleh pernyataan berikut: for i in range(5):\n","1. Mengulang dari 0 hingga 5 termasuk\n","2. Mengulang dari 1 hingga 5 termasuk\n","3. Mengulang dari 0 hingga 4\n","4. Mengulang dari 1 hingga 4\n","Jawaban Anda (masukkan nomor): 3\n","Benar!\n","\n","Tes Selesai! Skor Anda: 5 dari 5\n","Luar biasa! Anda memahami dasar Python dengan sangat baik.\n"]}]}]}