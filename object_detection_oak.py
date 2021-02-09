import depthai
device = depthai.Device('', False)
pipeline = device.create_pipeline(config={
    'streams': ['previewout', 'metaout'],
    'ai': {
        "blob_file": "/path/to/model.blob",
        "blob_file_config": "/path/to/config.json",
    },
})

