char END_OF_WORD = '.'; // indicates the end of a word

class Trie {
public:
    /** Initialize your data structure here. */
    Trie() {}
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        word += END_OF_WORD;
        Trie* curTrie = this; 
        int i, j; 
        for (i = 0; i < word.size(); i++)
        {
            char ch = word.at(i);
            for (j = 0; j < curTrie->children.size(); j++)
            {
                if (curTrie->children[j]->ch == ch)
                    break; 
            }
            if (j == curTrie->children.size()) // ch is not found in curTrie's children
            {
                Trie* newTrie = new Trie; 
                newTrie->ch = ch; 
                curTrie->children.push_back(newTrie); 
            }
            curTrie = curTrie->children[j]; 
        }
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        return searchWord(word+END_OF_WORD); 
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        return searchWord(prefix); 
    }

private:
    char ch; 
    vector<Trie*> children; 

    bool searchWord(string word)
    {
        Trie* curTrie = this;  
        int i, j; 
        for (i = 0; i < word.size(); i++)
        {
            char ch = word.at(i); 
            for (j = 0; j < curTrie->children.size(); j++)
            {   
                if (curTrie->children[j]->ch == ch)
                    break; 
            }
            if (j == curTrie->children.size()) // ch is not found in curTrie's children
                return false;
            curTrie = curTrie->children[j];  
        }
        return true; 
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */