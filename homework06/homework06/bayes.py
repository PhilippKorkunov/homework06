from math import log

class NaiveBayesClassifier:

    def __init__(self, alpha):
        self.alpha=alpha
        self.k=dict()
        self.b=[]
        pass

    def fit(self, X, y, d):
        k=len(d)
        k1=[]
        for i in range(k):
            k1.append(int(0))
        self.b=k1
        for i in range(len(y)):
            w=X[i].split()
            self.b[d[y[i]]]+=1
            for j in w:
                if j in self.k:
                    pass
                else:
                    self.k[j]= [0]*(2*k+1)
                self.k[j][d[y[i]]]+=1
                self.k[j][2*k]+=1
        d1=len(self.k)
        yc=[0]*k
        for i in self.k.keys():
            for j in range(k):
                yc[j]+=self.k[i][j]
        for i in self.k.keys():
            for j in range(k):
                self.k[i][k+j]=(self.k[i][j]+self.alpha)/(self.k[i][2*k]+self.alpha*d1)
        pass

    def predict(self, X):
        a=[]
        yc=len(self.b)
        for i in range(len(X)):
            w=X[i].split()
            p=[log(i) for i in self.b]
            for j in w:
                for o in range(yc):
                    if j not in self.k:
                        continue
                    p[o]+=log(self.k[j][yc+o])
            ind=0
            m=p[0]
            for j in range(1,yc):
                if p[j]>m:
                    m=p[j]
                    ind=j
            a.append(ind)
        return a

    def score(self, X_test, y_test,d):
        c=0
        a=[d[y] for y in y_test]
        p=self.predict(X_test)
        for i in range(len(y_test)):
            if p[i]==a[i]:
                c+=1
        b=c/len(y_test)
        return b
x = [
    "i love this sandwich",
    "this is an amazing place",
    "i feel very good about these beers",
    "this is my best work",
    "what an awesome view",
    "i do not like this restaurant",
    "i am tired of this stuff",
    "i cant deal with this",
    "he is my sworn enemy",
    "my boss is horrible",
]
y = [
    "Positive",
    "Positive",
    "Positive",
    "Positive",
    "Positive",
    "Negative",
    "Negative",
    "Negative",
    "Negative",
    "Negative",
]
x_test = [
    "the beer was good",
    "i do not enjoy my job",
    "i aint feeling dandy today",
    "i feel amazing",
    "gary is a friend of mine",
    "i cant believe im doing this",
]
y_test = ["Positive", "Negative", "Negative", "Positive", "Positive", "Negative"]
y_dict = {"Positive": 0, "Negative": 1}
test = NaiveBayesClassifier(0.1)
test.fit(x, y, y_dict)
# print(test.predict(x_test))
print(test.score(x_test, y_test, y_dict))