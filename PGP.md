Here’s a clear, step-by-step guide you can share with anyone who wants to **send me an encrypted file or message using PGP**:

---

## 🔐 How to Send Me Encrypted Data Using PGP

1. **Get My PGP Public Key**

   Option A – Download directly (if I’ve sent it to you):

   ```
   shaswat_shah_pub.asc
   ```

   Option B – Import from a keyserver (if published):

   ```bash
   gpg --keyserver hkps://keys.openpgp.org --recv-keys 0B9EF523BDC6F12E3DC149F78D4111372E48E8E8
   ```

---

2. **Verify My Key**

   Confirm the fingerprint matches:

   ```
   0B9E F523 BDC6 F12E 3DC1 49F7 8D41 1137 2E48 E8E8
   ```

---

3. **Encrypt a Message**

   To encrypt a short message:

   ```bash
   echo "Your secret message here" | gpg --armor --encrypt --recipient "shaswatshah05@gmail.com" > message.asc
   ```

   To encrypt a file:

   ```bash
   gpg --encrypt --recipient "shaswatshah05@gmail.com" secret_file.pdf
   ```

   This will create:

   ```
   secret_file.pdf.gpg
   ```

---

4. **Send Me the Encrypted Output**

   * If it's a message: send `message.asc`
   * If it’s a file: send `secret_file.pdf.gpg`

---

5. **Only I Can Decrypt It**

   Once encrypted using my public key, **only I (Shaswat) can decrypt it** using my private key.

---
