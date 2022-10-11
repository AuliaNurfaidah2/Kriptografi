import streamlit as st
from cryptography.hazmat.primitives import hashes

st.write("""
# Fungsi Hash
""")

input = st.text_input('Masukkan Teks', 'Aulia')

algoritma = st.selectbox('Fungsi Hash',('SHA224','SHA256', 'SHA384', 'SHA512', 'MD5', 'SHA1'))
if(algoritma == 'SHA224') :
    digest = hashes.Hash(hashes.SHA224())
elif(algoritma == 'SHA256') :
    digest = hashes.Hash(hashes.SHA256())
elif(algoritma == 'SHA384') :
    digest = hashes.Hash(hashes.SHA384())
elif(algoritma == 'SHA512') :
    digest = hashes.Hash(hashes.SHA512())
elif(algoritma == 'MD5') :
    digest = hashes.Hash(hashes.MD5())
else :
    digest = hashes.Hash(hashes.SHA1())

digest.update(input.encode())
hash = digest.finalize()
st.write('Hash :', hash.hex())