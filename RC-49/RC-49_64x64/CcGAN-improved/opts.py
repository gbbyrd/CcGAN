import argparse

def parse_opts():
    parser = argparse.ArgumentParser()

    ''' Overall Settings '''
    parser.add_argument('--root_path', type=str, default='/home/xin/OneDrive/Working_directory/CcGAN/RC-49-improved')
    parser.add_argument('--data_path', type=str, default='/home/xin/OneDrive/Working_directory/CcGAN/dataset/RC-49')
    parser.add_argument('--GAN', type=str, default='CcGAN', choices=['cGAN', 'CcGAN'])
    parser.add_argument('--seed', type=int, default=2020, metavar='S', help='random seed (default: 2020)')


    ''' Dataset '''
    ## Data split: RC-49 is split into a train set (the last decimal of the degree is odd) and a test set (the last decimal of the degree is even); the unique labels in two sets do not overlap.
    parser.add_argument('--data_split', type=str, default='train',
                        choices=['all', 'train'])
    parser.add_argument('--min_label', type=float, default=0.0)
    parser.add_argument('--max_label', type=float, default=90.0)
    parser.add_argument('--num_channels', type=int, default=3, metavar='N')
    parser.add_argument('--img_size', type=int, default=64, metavar='N',
                        choices=[64])
    parser.add_argument('--max_num_img_per_label', type=int, default=50, metavar='N')
    parser.add_argument('--max_num_img_per_label_after_replica', type=int, default=0, metavar='N')
    parser.add_argument('--show_real_imgs', action='store_true', default=False)
    parser.add_argument('--visualize_fake_images', action='store_true', default=False)


    ''' GAN settings '''
    # label embedding setting
    parser.add_argument('--net_embed', type=str, default='ResNet34_embed') #ResNetXX_emebed
    parser.add_argument('--epoch_cnn_embed', type=int, default=200) #epoch of cnn training for label embedding
    parser.add_argument('--resumeepoch_cnn_embed', type=int, default=0) #epoch of cnn training for label embedding
    parser.add_argument('--epoch_net_y2h', type=int, default=500)
    parser.add_argument('--dim_embed', type=int, default=512) #dimension of the embedding space
    parser.add_argument('--batch_size_embed', type=int, default=256, metavar='N')

    parser.add_argument('--loss_type_gan', type=str, default='vanilla')
    parser.add_argument('--niters_gan', type=int, default=10000, help='number of iterations')
    parser.add_argument('--resume_niters_gan', type=int, default=0)
    parser.add_argument('--save_niters_freq', type=int, default=2000, help='frequency of saving checkpoints')
    parser.add_argument('--lr_g_gan', type=float, default=1e-4, help='learning rate for generator')
    parser.add_argument('--lr_d_gan', type=float, default=1e-4, help='learning rate for discriminator')
    parser.add_argument('--dim_gan', type=int, default=128, help='Latent dimension of GAN')
    parser.add_argument('--batch_size_disc', type=int, default=64)
    parser.add_argument('--batch_size_gene', type=int, default=64)
    parser.add_argument('--cGAN_num_classes', type=int, default=90, metavar='N') #bin label into cGAN_num_classes

    parser.add_argument('--kernel_sigma', type=float, default=-1.0,
                        help='If kernel_sigma<0, then use rule-of-thumb formula to compute the sigma.')
    parser.add_argument('--threshold_type', type=str, default='hard', choices=['soft', 'hard'])
    parser.add_argument('--kappa', type=float, default=-1)
    parser.add_argument('--nonzero_soft_weight_threshold', type=float, default=1e-3,
                        help='threshold for determining nonzero weights for SVDL; we neglect images with too small weights')


    # evaluation setting
    '''
    Four evaluation modes:
    Mode 1: eval on unique labels used for GAN training;
    Mode 2. eval on all unique labels in the dataset and when computing FID use all real images in the dataset;
    Mode 3. eval on all unique labels in the dataset and when computing FID only use real images for GAN training in the dataset (to test SFID's effectiveness on unseen labels);
    Mode 4. eval on a interval [min_label, max_label] with num_eval_labels labels.
    '''
    parser.add_argument('--eval_mode', type=int, default=2)
    parser.add_argument('--num_eval_labels', type=int, default=-1)
    parser.add_argument('--samp_batch_size', type=int, default=1000)
    parser.add_argument('--nfake_per_label', type=int, default=200)
    parser.add_argument('--nreal_per_label', type=int, default=-1)
    parser.add_argument('--comp_FID', action='store_true', default=False)
    parser.add_argument('--epoch_FID_CNN', type=int, default=200)
    parser.add_argument('--FID_radius', type=float, default=0)
    parser.add_argument('--FID_num_centers', type=int, default=-1)
    parser.add_argument('--dump_fake_for_NIQE', action='store_true', default=False)
    parser.add_argument('--comp_IS_and_FID_only', action='store_true', default=False)

    args = parser.parse_args()

    return args
