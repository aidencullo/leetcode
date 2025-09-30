struct Solution;

impl Solution {
    pub fn reverse_vowels(s: String) -> String {
        for c in s.chars() {
            println!("{}", c);
        }
        s // return the original string to satisfy type
    }
}

fn main() {
    let s = "hello".to_string();
    Solution::reverse_vowels(s);
}
