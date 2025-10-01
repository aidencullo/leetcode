impl Solution {
    pub fn reverse_vowels(s: String) -> String {
        let possible_vowels = "aeiouAEIOU";
        let mut result = String::new();
        let mut vowels = String::new();

        for c in s.chars() {
            if possible_vowels.contains(c) {
                vowels.push(c);
            }
        }

        for c in s.chars() {
            if possible_vowels.contains(c) {
                result.push(vowels.pop().unwrap());
            } else {
                result.push(c);
            }
        }

        result
    }
}
