use nokhwa::{Camera, CameraFormat, CaptureAPIBackend, FrameFormat};

fn main() {
    let devices = nokhwa::query_devices(CaptureAPIBackend::GStreamer);
    println!("devices:");
    for device in devices{
        println!("{device:?}")
    }
    let mut webcam = Camera::new(
        0, // index
        Some(CameraFormat::new_from(640, 480, FrameFormat::MJPEG, 30)), // format
    ).unwrap();

    let decoder = bardecoder::default_decoder();

    loop {
        let frame = webcam.frame().unwrap();

    }
}