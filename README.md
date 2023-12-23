# Bot Anti-Broadcast Telegram

Bot ini dibuat menggunakan Python dengan bantuan pustaka python-telegram-bot. Bot ini dapat digunakan untuk menghapus pesan broadcast atau global di grup Telegram.
[![Deploy](https://www.herokucdn.com/deploy/button.svg)

## Persiapan

1. **Bot Telegram:**
   - Buat bot Telegram dengan menghubungi [BotFather](https://t.me/botfather).
   - Dapatkan token bot dari BotFather.

2. **Repositori GitHub:**
   - Buat repositori baru di GitHub.

3. **Heroku:**
   - Daftar dan buat aplikasi di [Heroku](https://www.heroku.com/).

## Konfigurasi

1. **Heroku:**
   - Pada tab "Settings" di Heroku, tambahkan variabel lingkungan:
     - `BOT_TOKEN`: Token bot yang Anda dapatkan dari BotFather.
     - `CHAT_ID`: ID grup di Telegram.
     
2. **GitHub Secrets:**
   - Pada halaman repositori GitHub, buka tab "Settings" -> "Secrets", dan tambahkan variabel:
     - `BOT_TOKEN`: Token bot yang Anda dapatkan dari BotFather.
     - `CHAT_ID`: ID grup di Telegram.

## Deploy ke Heroku

1. Hubungkan aplikasi Heroku ke repositori GitHub.
2. Pilih metode deploy dari GitHub di tab "Deploy" di Heroku.
3. Aktifkan "Automatic Deploys" jika diinginkan.

## Menjalankan Bot Lokal (Opsional)

Jika ingin menjalankan bot secara lokal:

1. Install dependensi dengan menjalankan `pip install -r requirements.txt`.
2. Setel variabel lingkungan `BOT_TOKEN` dan `CHAT_ID`.
3. Jalankan bot dengan perintah `python bot.py`.

## Catatan

- Pastikan bot memiliki izin untuk menghapus pesan di grup Telegram.

Terima kasih telah menggunakan Bot Anti-Broadcast Telegram!
