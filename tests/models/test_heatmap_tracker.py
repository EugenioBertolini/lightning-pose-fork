"""Test the initialization and training of heatmap models."""

import copy

from lightning_pose.utils.tests import run_model_test


def test_supervised_heatmap(
    cfg, heatmap_data_module, video_dataloader, trainer, remove_logs,
):
    """Test the initialization and training of a supervised heatmap model."""

    cfg_tmp = copy.deepcopy(cfg)
    cfg_tmp.model.model_type = "heatmap"
    cfg_tmp.model.losses_to_use = []

    run_model_test(
        cfg=cfg_tmp,
        data_module=heatmap_data_module,
        video_dataloader=video_dataloader,
        trainer=trainer,
        remove_logs_fn=remove_logs,
    )


def test_semisupervised_heatmap_temporal(
    cfg,
    heatmap_data_module_combined,
    video_dataloader,
    trainer,
    remove_logs,
):
    """Test the initialization and training of a semi-supervised heatmap model."""

    cfg_tmp = copy.deepcopy(cfg)
    cfg_tmp.model.model_type = "heatmap"
    cfg_tmp.model.losses_to_use = ["temporal", "pca_singleview"]

    run_model_test(
        cfg=cfg_tmp,
        data_module=heatmap_data_module_combined,
        video_dataloader=video_dataloader,
        trainer=trainer,
        remove_logs_fn=remove_logs,
    )
