#include <string>
#include <opus/opus.h>


using namespace std;

class CompressionHandler {
    public:
        CompressionHandler(opus_int32 sampling_rate, int channels, int application, 
                        int max_data_bytes, int frame_size);
        //    ~CompressionHandler();

        opus_int32 encode_float(const float *input_pcm, unsigned char *compressed_data);
        int decode_float(const unsigned char *input_data, int input_bytes, float *pcm);
        
    private:
        OpusEncoder *_encoder;
        OpusDecoder *_decoder;
        opus_int32 sampling_rate;
        int channels;
        int application;
        int frame_size;
        opus_int32 max_data_bytes;

        void opus_error(int error_code, string message);
};

