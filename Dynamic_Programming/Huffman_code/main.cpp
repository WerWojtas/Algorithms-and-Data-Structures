#include <iostream>
#include <fstream>
#include <unordered_map>
#include <string>
using namespace ::std;

void save_text_to_bits(unordered_map<char,string> hash_map);

int main() {
    ifstream file;
    file.open("C:\\Users\\weron\\OneDrive\\Pulpit\\Kod_huffmana\\code.txt");
    if(file.good()){
        unordered_map<char, string> char_to_prefix_map;
        string prefix;
        char character;

        while (file >> character) {
            getline(file, prefix);
            char_to_prefix_map[character] = prefix;
        }
        file.close();
        save_text_to_bits(char_to_prefix_map);
    }
    else{
        cout<<"Cannot open code file";
    }
    return 0;
}


void save_text_to_bits(unordered_map<char,string> hash_map){
    ifstream file;
    file.open("C:\\Users\\weron\\OneDrive\\Pulpit\\Kod_huffmana\\kod_huffmana.txt");
    ofstream bit_file("C:\\Users\\weron\\OneDrive\\Pulpit\\Kod_huffmana\\bin_code.txt",ios::binary);
    char sign;
    cout<<"S";
    string prefix_code;
    unsigned char current_byte=0;
    int bit_count=0;
    if(file.good() && bit_file.good()){
        while(!file.eof()){
            file.get(sign);
            prefix_code=hash_map[sign];
            for(char bit : prefix_code){
                if (bit == '1') {
                    current_byte |= (1 << bit_count);
                }
                bit_count++;
                if(bit_count==8){
                    bit_file.write(reinterpret_cast<char*>(&current_byte), sizeof(current_byte));
                    current_byte=0;
                    bit_count=0;
                }
            }
        }
        if (bit_count > 0) {
            bit_file.write(reinterpret_cast<char*>(&current_byte), sizeof(current_byte));
        }
        bit_file.close();

    }
    else{
        cout<<"Cannot open one of the files";
    }
}