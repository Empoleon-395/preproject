from sklearn.semi_supervised import LabelSpreading
class my_labspread:
    def __init__(self,kernel="knn",n_neighbors=11,alpha=0.2):
        self.model=LabelSpreading(kernel=kernel, alpha=alpha, n_neighbors=n_neighbors,max_iter=1000, n_jobs=-1)

    def fit(self,x_data,y_data):
        self.model.fit(x_data,y_data)

    def return_pre_lab(self,x_data):
        rt_lab=self.model.predict(x_data)
        return rt_lab
