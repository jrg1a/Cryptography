using System;
using System.IO;
using System.Security.Cryptography;
using System.Text;

class AESExample
{
    public static byte[] EncryptStringToBytes(string plainText, byte[] key, byte[] iv)
    {
        if (string.IsNullOrEmpty(plainText))
            throw new ArgumentNullException(nameof(plainText));
        if (key == null || key.Length <= 0)
            throw new ArgumentNullException(nameof(key));
        if (iv == null || iv.Length <= 0)
            throw new ArgumentNullException(nameof(iv));

        byte[] encrypted;
        using (Aes aes = Aes.Create())
        {
            aes.Key = key;
            aes.IV = iv;
            ICryptoTransform encryptor = aes.CreateEncryptor(aes.Key, aes.IV);
            using (MemoryStream msEncrypt = new MemoryStream())
            {
                using (CryptoStream csEncrypt = new CryptoStream(msEncrypt, encryptor, CryptoStreamMode.Write))
                {
                    using (StreamWriter swEncrypt = new StreamWriter(csEncrypt))
                    {
                        swEncrypt.Write(plainText);
                    }
                    encrypted = msEncrypt.ToArray();
                }
            }
        }
        return encrypted;
    }

    public static string DecryptStringFromBytes(byte[] cipherText, byte[] key, byte[] iv)
    {
        if (cipherText == null || cipherText.Length <= 0)
            throw new ArgumentNullException(nameof(cipherText));
        if (key == null || key.Length <= 0)
            throw new ArgumentNullException(nameof(key));
        if (iv == null || iv.Length <= 0)
            throw new ArgumentNullException(nameof(iv));

        string plaintext;
        using (Aes aes = Aes.Create())
        {
            aes.Key = key;
            aes.IV = iv;
            ICryptoTransform decryptor = aes.CreateDecryptor(aes.Key, aes.IV);
            using (MemoryStream msDecrypt = new MemoryStream(cipherText))
            {
                using (CryptoStream csDecrypt = new CryptoStream(msDecrypt, decryptor, CryptoStreamMode.Read))
                {
                    using (StreamReader srDecrypt = new StreamReader(csDecrypt))
                    {
                        plaintext = srDecrypt.ReadToEnd();
                    }
                }
            }
        }
        return plaintext;
    }

    public static void Main(string[] args)
    {
        try
        {
            using (Aes myAes = Aes.Create())
            {
                // Encrypt the string to an array of bytes.
                byte[] encrypted = EncryptStringToBytes("This is a test message.", myAes.Key, myAes.IV);

                // Decrypt the bytes to a string.
                string decrypted = DecryptStringFromBytes(encrypted, myAes.Key, myAes.IV);

                Console.WriteLine($"Original: This is a test message.");
                Console.WriteLine($"Encrypted: {BitConverter.ToString(encrypted)}");
                Console.WriteLine($"Decrypted: {decrypted}");
            }
        }
        catch (Exception e)
        {
            Console.WriteLine($"Error: {e.Message}");
        }
    }
}
