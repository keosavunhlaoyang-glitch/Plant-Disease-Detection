def get_info(label):
    
    data = {

        # Rice
        "rice___healthy": {
            "lo": "ໃບເຂົ້າສຸຂະພາບດີ (Healthy)"
        },

        "rice___leaf_blast": {
            "lo": "ພະຍາດເຂົ້າໃບໄໝ້ (Leaf Blast)"
        },

        "rice___brown_spot": {
            "lo": "ພະຍາດເຂົ້າໃບຈຸດສີນ້ຳຕານ (Brown Spot)"
        },

        "rice___bacterial_leaf_blight": {
            "lo": "ພະຍາດເຂົ້າໃບແຫ້ງ (Bacterial Leaf Blight)"
        },

        # Corn
        "corn___healthy": {
            "lo": "ໃບສາລີສຸຂະພາບດີ (Healthy)"
        },

        "corn___leaf_blight": {
            "lo": "ພະຍາດສາລີໃບໄໝ້ (Leaf Blight)"
        },

        "corn___gray_leaf_spot": {
            "lo": "ພະຍາດສາລີໃບຈຸດສີເທົາ (Gray Leaf Spot)"
        },

        "corn___common_rust": {
            "lo": "ພະຍາດສາລີໃບຂີ້ມ້ຽງ (Common Rust)"
        },

        # Cucumber
        "cucumber___healthy": {
            "lo": "ໃບໝາກແຕງສຸຂະພາບດີ (Healthy)"
        },

        "cucumber___downy_mildew": {
            "lo": "ພະຍາດໝາກແຕງລານ້ຳຄ້າງ (Downy Mildew)"
        },

        "cucumber___gummy_stem_blight": {
            "lo": "ພະຍາດໝາກແຕງຕົ້ນແຕກຍາງໄຫຼ (Gummy Stem Blight)"
        },

        "cucumber___anthracnose": {
            "lo": "ພະຍາດໝາກແຕງໃບຈຸດດ່າງ (Anthracnose)"
        },

        "ບໍ່ຮູ້ຈັກ": {
            "lo": "ບໍ່ຮູ້ຈັກ (Unknown)"
       }
    }

    return data.get(label, {
        "lo": label
    })