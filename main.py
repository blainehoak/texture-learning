import torch
import torchvision as tv
from torchvision import models
import torchvision.transforms as T
import json
import pandas as pd
import numpy as np
import argparse


def get_dataloader(batch_size=120):
    data_kwargs = (
        {"num_workers": 4, "pin_memory": True}
        if device == "cuda"
        else {"num_workers": 8}
    )
    MEAN = np.array([0.485, 0.456, 0.406])
    STD = np.array([0.229, 0.224, 0.225])
    normalize = T.Normalize(mean=MEAN, std=STD)
    preprocessing = T.Compose(
        [T.Resize(256), T.CenterCrop(224), T.ToTensor(), normalize]
    )

    dtds = [
        tv.datasets.DTD(
            root=".", split="train", transform=preprocessing, download=True
        ),
        tv.datasets.DTD(root=".", split="val", transform=preprocessing, download=True),
        tv.datasets.DTD(root=".", split="test", transform=preprocessing, download=True),
    ]
    dataset = torch.utils.data.ConcatDataset(dtds)
    dataloader = torch.utils.data.DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=True,
        **data_kwargs,
    )
    return dataloader, dtds


def main(maxk=3):
    model = models.resnet50(weights="DEFAULT").eval().to(device)
    dataloader, dtds = get_dataloader()
    conf_mat = torch.zeros(47, 1000).to(device)
    for x, y in dataloader:
        x, y = x.to(device), y.to(device)
        y_pred = model(x).argmax(1)
        conf_mat[y, y_pred] += 1
    with open("imagenet_class_index.json") as f:
        classes_json = json.load(f)
    imagenet_classes = [classes_json[str(k)][1] for k in range(1000)]

    dim = 1
    conf_mat_norm = conf_mat / conf_mat.sum(dim=dim, keepdim=True)
    conf_mat_norm_topk = conf_mat_norm.cpu().topk(maxk, dim=dim)
    df_dict = {"texture class": dtds[0].classes}
    for k in range(maxk):
        df_dict[f"imagenet class top {k+1}"] = [
            imagenet_classes[conf_mat_norm_topk.indices[i, k]] for i in range(47)
        ]
        df_dict[f"effect size top {k+1}"] = conf_mat_norm_topk.values[:, k]
    df = pd.DataFrame(df_dict)
    df.sort_values("effect size top 1", ascending=False).to_csv(
        f"texture_object_top{maxk}.csv"
    )


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--maxk", type=int, default=3)
    args = argparser.parse_args()
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")
    if device == "cuda":
        torch.hub.set_dir(".")
    main(args.maxk)
