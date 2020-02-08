#include <iostream>
#include <stdlib.h>
#include <string>
#include <opus/opus.h>
#include "compressionHandler.h"


using namespace std;


void CompressionHandler::opus_error(int error=0, string message="") {
    fprintf(stderr, "Error code: %d\n", error);
    fprintf(stderr, "Error message: %s\n", opus_strerror(error));
    cout << message << endl;
    exit(84);
}


CompressionHandler::CompressionHandler(opus_int32 sampling_rate, int channels, 
                                       int application, int max_data_bytes, int frame_size) {
    /* Regardless of the sampling rate and number channels selected,
    * the Opus encoder can switch to a lower audio bandwidth or number of channels if the bitrate selected is too low.
    * This also means that it is safe to always use 48 kHz stereo input and let the encoder optimize the encoding.
    */
    this -> sampling_rate = sampling_rate;    
    this -> channels = channels;
    this -> application = application; 
    this -> max_data_bytes = max_data_bytes;    
    this -> frame_size = frame_size; 

    int error;
    _encoder = opus_encoder_create(sampling_rate, channels, application, &error);
    if (error != OPUS_OK) {
        opus_error(error, "Failed to create an encoder.");
    }
    this -> _encoder = _encoder;

    _decoder = opus_decoder_create(sampling_rate, channels, &error);
    if (error != OPUS_OK) {
        opus_error(error, "Failed to create a decoder.");
    }
    this -> _decoder = _decoder;
}


opus_int32 CompressionHandler::encode_float(const float *input_pcm, unsigned char* compressed){
    /*      Parameters
     * pcm    float*: Input in float format (interleaved if 2 channels), with a normal range of +/-1.0. Samples with a range beyond +/-1.0 are supported but will be clipped by decoders using the integer API and should only be used if it is known that the far end supports extended dynamic range. length is frame_size*channels*sizeof(float)
     * frame_size    int: Number of samples per channel in the input signal. This must be an Opus frame size for the encoder's sampling rate. For example, at 48 kHz the permitted values are 120, 240, 480, 960, 1920, and 2880. Passing in a duration of less than 10 ms (480 samples at 48 kHz) will prevent the encoder from using the LPC or hybrid modes.
     * data    unsigned char*: Output payload. This must contain storage for at least max_data_bytes.
     * max_data_bytes    opus_int32: Size of the allocated memory for the output payload. This may be used to impose an upper limit on the instant bitrate, but should not be used as the only bitrate control. Use OPUS_SET_BITRATE to control the bitrate.
     *
     *      Returns
     * The length of the encoded packet (in bytes) on success or a negative error code (see Error codes) on failure.
     */
    compressed = new unsigned char[max_data_bytes];

    opus_int32 error, packet_length;
    error = opus_encode_float(this->_encoder, input_pcm, 
                              this->frame_size, compressed, this->max_data_bytes);
    if (error < 0) {
        opus_error(error, "Failed to encode the float.\n");
    }
    packet_length = error;
    return packet_length;
}


template <typename T>
void print_array(T *arr, int N) {
    printf("Printing array with size=%d:\n", N);
    bool dots = true;
    for (int i = 0; i < N; i++) {
        auto value = arr[i];
        if (i < 5 || i > (N-5)) {
            cout << value << ", ";
        } else if (dots) {
            cout << " ... ";
            dots = false;
        }
    }
    cout << "\n";
}


int CompressionHandler::decode_float(const unsigned char *input_data, int input_bytes, float *pcm) {
    int error, decoded_samples;
    print_array(input_data, input_bytes);
    print_array(pcm, frame_size*channels);
    error = opus_decode_float(_decoder, input_data, input_bytes, pcm, frame_size, 1);
    if (error < 0) {
        opus_error(error, "Failed to decode the float.\n");
    }
    print_array(pcm, frame_size*channels);
    decoded_samples = error;
    return decoded_samples;
}