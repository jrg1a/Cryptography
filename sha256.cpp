#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <crypto++/sha.h>
#include <crypto++/hex.h>
#include <crypto++/files.h>

using namespace CryptoPP;

int main(int argc, char *argv[])
{
    if (argc != 3)
    {
        std::cout << "Usage: " << argv[0] << " <input_file> <output_file>" << std::endl;
        return 1;
    }

    std::string input_file = argv[1];
    std::string output_file = argv[2];

    try
    {
        SHA256 hash;
        std::string digest;

        FileSource f(input_file.c_str(), true,
                     new HashFilter(hash,
                                    new HexEncoder(new StringSink(digest), false)));

        std::ofstream output(output_file);
        if (output.is_open())
        {
            output << digest;
            output.close();
        }
        else
        {
            std::cout << "Unable to open output file." << std::endl;
            return 1;
        }
    }
    catch (const Exception &ex)
    {
        std::cerr << "Error: " << ex.what() << std::endl;
        return 1;
    }

    return 0;
}
