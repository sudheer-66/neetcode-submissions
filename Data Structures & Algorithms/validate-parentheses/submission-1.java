class Solution {
    public boolean isValid(String s) {

        Deque<Character> stack = new ArrayDeque<>();
        //String st = new String("{[(");
        Set<Character> st = new HashSet<>(Arrays.asList('{','[','('));

        for(char c : s.toCharArray()){
            if(st.contains(c)){
                stack.push(c);
            }
            else{
                Character ct = stack.peek();
                if(ct==null || (c=='}' && ct!='{') || (c==']' && ct!='[') || (c==')' && ct!='(')){
                    return false;
                }
                stack.pop();
            }
        }
        return stack.isEmpty();
        
    }
}
