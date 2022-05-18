# **Encryption Algorithm Using Numpy**

---

## DO NOT USE THIS TO ENCRYPT AND STORE IMPORTANT TEXT. IT'S SECURITY HAS NOT BEEN TESTED.

---

**Dependencies:**

pip install charcade

pip install numpy

---

### **_How encryption works:_**

This is an encryption algorithm created using numpy.
Numpy is used to generate an array of numbers 0-94 that is organized in a 19 x 5 2D array.
the array is then shuffled up, down, left and right (kinda like a rubiks cube) a random number of times.

After the array is shuffled, the numbers are converted into a list and letters from the alphabet
are placed in their index position. After that the text that you input is ciphered using the generated
alphabet and the encrypted text and key are printed in the terminal.

<img src="pictures/enc1.png" width="400"/>

---

<img src="pictures/enc2.png" width="470"/>

---

<img src="pictures/enc3.png" width="600"/>

---

---

### **_How decryption works:_**

The decryptor remakes the alphabet using 2 parts of the key and the third part of the key determines
the reverse shift in the cipher after the alphabet is reconstructed.

<img src="pictures/dec1.png" width="400"/>

---

<img src="pictures/dec2.png" width="450"/>

---

<img src="pictures/dec3.png" width="600"/>
