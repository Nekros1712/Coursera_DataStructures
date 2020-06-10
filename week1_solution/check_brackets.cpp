#include <iostream>
#include <stack>
#include <string>
using namespace std;

struct Bracket {
    Bracket(char type, int position):
        type(type),
        position(position)
    {}

    bool Matchc(char c) {
        if (type == '[' && c == ']')
            return true;
        if (type == '{' && c == '}')
            return true;
        if (type == '(' && c == ')')
            return true;
        return false;
    }

    char type;
    int position;
};

int main() {
    std::string text;
    getline(std::cin, text);

    std::stack <Bracket> opening_brackets_stack;
	int pos=0;
    for (int position = 0; position < text.length(); ++position) {
        char next = text[position];

        if (next == '(' || next == '[' || next == '{') {
            // Process opening bracket, write your code here
			Bracket* curr = new Bracket(next,position+1);
            opening_brackets_stack.push(*curr);
        }

        if (next == ')' || next == ']' || next == '}') {
            // Process closing bracket, write your code here
			if(opening_brackets_stack.empty()){
                pos = position+1;
                break;
            }
            Bracket top = opening_brackets_stack.top();
            opening_brackets_stack.pop();
            if(!top.Matchc(next)){
                pos = position+1;
                break;
            }
        }
    }

    // Printing answer, write your code here
	if(pos == 0 && opening_brackets_stack.empty()){
        cout << "Success";
    }else if(pos == 0){
        while(opening_brackets_stack.size() > 1)
            opening_brackets_stack.pop();
        pos = opening_brackets_stack.top().position;
        cout << pos;
    }else{
        cout << pos;
    }

    return 0;
}
