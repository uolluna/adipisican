import pickle

# assume dict_all is your edges dictionary
with open('edges.pkl', 'wb') as f:
    pickle.dump(dict_all, f)
