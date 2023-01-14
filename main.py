
def main(synonyms):

    group = {};
    visited = {};

    for i in synonyms:

        for j in i:

            if j not in group:
                group[j] = [];
                visited[j] = 0;
            
            if i[j] not in group:
                group[i[j]] = [];
                visited[i[j]] = 0;

            group[j].append(i[j]);
            group[i[j]].append(j);

    
    def dfs(a,word):
        nonlocal visited;

        if visited[word] == 1:
            return;

        a.append(word);
        visited[word] = 1;

        for j in group[word]:
            dfs(a,j);


    output = [];

    for i in group:

        t = [];
        dfs(t,i);

        if len(t):
            output.append(t);

    return output;


print(main([ {"Dg set": "Diesel generator"}, {"Organization": "Organisation"}, {"Group": "Organization"}, {"Orange": "Kinnu"}, {"Orange": "narangi"} ] ))