from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Mengizinkan koneksi dari halaman HTML pelanggan & admin
CORS(app)

# Memori sementara untuk menampung pesanan (bisa diganti database nanti)
DATABASE_PESANAN = []

@app.route('/api/pesanan', methods=['GET', 'POST'])
def kelola_pesanan():
    if request.method == 'POST':
        data = request.json
        if not data:
            return jsonify({"status": "error", "message": "Data kosong"}), 400
        
        # Simpan pesanan masuk ke memori server
        DATABASE_PESANAN.append(data)
        return jsonify({"status": "success", "message": "Pesanan berhasil direkam server!"}), 201
    
    # Jika GET (Admin meminta data), kirim semua rekapan pesanan
    return jsonify(DATABASE_PESANAN)

@app.route('/api/pesanan/clear', methods=['POST'])
def hapus_pesanan():
    global DATABASE_PESANAN
    DATABASE_PESANAN = []
    return jsonify({"status": "success", "message": "Database berhasil dikosongkan"})

if __name__ == '__main__':
    # Berjalan di port 5050
    app.run(host='0.0.0.0', port=5050, debug=True)