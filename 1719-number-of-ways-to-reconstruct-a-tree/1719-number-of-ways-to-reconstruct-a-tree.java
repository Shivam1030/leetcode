class Solution {
    public int checkWays(int[][] pairs) {
        System.out.println(pairs.length);
        HashMap<Integer, Set<Integer>> map = new HashMap<>();
        HashMap<Integer, Integer> prt = new HashMap<>();
        sum = 0;
        
        for(int[] pair:pairs){
            if(!map.containsKey(pair[0])){
                map.put(pair[0], new HashSet<>());
                prt.put(pair[0], pair[0]);
            }
            if(!map.containsKey(pair[1])){
                map.put(pair[1], new HashSet<>());
                prt.put(pair[1], pair[1]);
            }
            map.get(pair[0]).add(pair[1]);
            map.get(pair[1]).add(pair[0]);
        }

        HashMap<Integer, ArrayList<Integer>> adj = new HashMap<>();
        int root = -1;
        while(!map.isEmpty()){
            int ele = -1;
            int sz = -1;
            for(int ky: map.keySet()){
                if(sz < map.get(ky).size()){
                    sz = map.get(ky).size();
                    ele = ky;
                }
            }
            if(root == -1) {
                root = ele;
                if(sz != prt.size()-1) return 0;
            }
            
            if(!adj.containsKey(ele)) adj.put(ele, new ArrayList<>());
            if(ele != prt.get(ele)){
                adj.get(prt.get(ele)).add(ele);
            }

            for(int num: map.get(ele)){
                prt.replace(num, ele);
                map.get(num).remove(ele);
            }

            map.remove(ele);
        }

        validity(adj, root, 0);
        if(sum != pairs.length) return 0;
        
        for(ArrayList<Integer> ele: adj.values()){
            if(ele.size() == 1) return 2;
        }
        
        return 1;
    }
    
    int sum;
    public void validity(HashMap<Integer, ArrayList<Integer>> map, int node, int cnt){
        for(int nxt: map.get(node)){
            validity(map, nxt, cnt+1);
        }
        
        sum += cnt;
    }
}