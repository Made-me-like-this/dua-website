from django.core.management.base import BaseCommand
from myapp.models import Category, Dua

class Command(BaseCommand):
    help = 'Populates the database with initial dua data'

    def handle(self, *args, **kwargs):
        # Check if there's already data
        if Category.objects.exists():
            self.stdout.write(self.style.WARNING('Data already exists, skipping population'))
            return

        # Create categories
        morning_evening = Category.objects.create(
            name='Morning & Evening Duas',
            description='Duas to recite in the morning and evening for protection and blessings'
        )

        salah = Category.objects.create(
            name='Salah (Prayer)',
            description='Duas related to prayer, including before, during, and after prayer'
        )

        home = Category.objects.create(
            name='Home & Family',
            description='Duas for home, family, marriage, and children'
        )

        travel = Category.objects.create(
            name='Travel Duas',
            description='Duas for journeys, including before travel, during travel, and after return'
        )

        protection = Category.objects.create(
            name='Protection Duas',
            description='Duas for seeking protection from evil, harm, and distress'
        )

        forgiveness = Category.objects.create(
            name='Forgiveness & Repentance',
            description='Duas for seeking forgiveness and turning back to Allah'
        )

        sleeping = Category.objects.create(
            name='Sleeping & Waking',
            description='Duas for when going to sleep and waking up'
        )

        food = Category.objects.create(
            name='Food & Eating',
            description='Duas related to food, before and after eating'
        )

        masjid = Category.objects.create(
            name='Masjid',
            description='Duas for entering and leaving the mosque'
        )

        emotional = Category.objects.create(
            name='Emotional Wellbeing',
            description='Duas for anxiety, anger, sorrow, and emotional distress'
        )

        ramadan = Category.objects.create(
            name='Ramadan',
            description='Duas for fasting, taraweeh, and other Ramadan practices'
        )

        guidance = Category.objects.create(
            name='Guidance & Decision Making',
            description='Duas for seeking guidance and making decisions'
        )

        # Original Duas from Python file
        Dua.objects.create(
            title='Morning/Evening Remembrance',
            arabic_text='أَصْبَحْنَا وَأَصْبَحَ الْمُلْكُ لِلَّهِ، وَالْحَمْدُ لِلَّهِ، لاَ إِلَٰهَ إِلاَّ اللهُ وَحْدَهُ لاَ شَرِيكَ لَهُ، لَهُ الْمُلْكُ وَلَهُ الْحَمْدُ وَهُوَ عَلَى كُلِّ شَيْءٍ قَدِيرٌ.',
            transliteration='Asbahna wa asbahal mulku lillah walhamdu lillah, la ilaha illallahu wahdahu la shareeka lah, lahul mulku wa lahul hamd, wa huwa \'ala kulli shay\'in qadeer.',
            translation='We have reached the morning and the kingdom of Allah has reached the morning. Praise is to Allah. None has the right to be worshipped except Allah, alone, without partner. To Him belongs the dominion and to Him belongs all praise, and He is over all things Omnipotent.',
            reference='Muslim',
            category=morning_evening,
            benefit='To be said in the morning. For evening, replace "asbahna" with "amsayna".'
        )

        Dua.objects.create(
            title='Seeking Protection in the Morning/Evening',
            arabic_text='اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنَ الْهَمِّ وَالْحَزَنِ، وَأَعُوذُ بِكَ مِنَ الْعَجْزِ وَالْكَسَلِ، وَأَعُوذُ بِكَ مِنَ الْجُبْنِ وَالْبُخْلِ، وَأَعُوذُ بِكَ مِنْ غَلَبَةِ الدَّيْنِ، وَقَهْرِ الرِّجَالِ.',
            transliteration="Allahumma inni a'udhu bika minal-hammi walhuzn, wa a'udhu bika minal-'ajzi wal-kasal, wa a'udhu bika minal-jubni wal-bukhl, wa a'udhu bika min ghalabatid-dayni wa qahrir-rijal.",
            translation='O Allah, I seek refuge in You from anxiety and sorrow, weakness and laziness, miserliness and cowardice, the burden of debts and from being overpowered by men.',
            reference='Bukhari',
            category=morning_evening,
            benefit='This dua provides protection from negative emotions and situations.'
        )

        Dua.objects.create(
            title='Opening Dua in Prayer (Istiftah)',
            arabic_text='سُبْحَانَكَ اللَّهُمَّ وَبِحَمْدِكَ، وَتَبَارَكَ اسْمُكَ، وَتَعَالَى جَدُّكَ، وَلاَ إِلَهَ غَيْرُكَ.',
            transliteration='Subhanakallahumma wa bihamdika, wa tabarakasmuka, wa ta\'ala jadduka, wa la ilaha ghairuk.',
            translation='Glory is to You, O Allah, and praise. Blessed is Your name and exalted is Your majesty. There is no god but You.',
            reference='Abu Dawud, Tirmidhi',
            category=salah,
            benefit='To be recited after Takbeer Tahreema (opening takbeer) in prayer.'
        )

        Dua.objects.create(
            title='Dua in Ruku (Bowing)',
            arabic_text='سُبْحَانَ رَبِّيَ الْعَظِيمِ.',
            transliteration='Subhana Rabbiyal-Adheem.',
            translation='Glory is to my Lord, the Most Great.',
            reference='Muslim',
            category=salah,
            benefit='To be recited at least three times while bowing in prayer.'
        )

        Dua.objects.create(
            title='Dua Before Entering Home',
            arabic_text='بِسْمِ اللَّهِ وَلَجْنَا، وَبِسْمِ اللَّهِ خَرَجْنَا، وَعَلَى رَبِّنَا تَوَكَّلْنَا.',
            transliteration='Bismillahi walajna, wa bismillahi kharajna, wa \'ala Rabbina tawakkalna.',
            translation='In the name of Allah we enter, in the name of Allah we leave, and upon our Lord we depend.',
            reference='Abu Dawud',
            category=home,
            benefit='To be recited when entering home for protection and blessings.'
        )

        Dua.objects.create(
            title='Dua for Newlyweds',
            arabic_text='بَارَكَ اللَّهُ لَكَ، وَبَارَكَ عَلَيْكَ، وَجَمَعَ بَيْنَكُمَا فِي خَيْرٍ.',
            transliteration='Barakallahu laka, wa baraka \'alaika, wa jama\'a bainakuma fee khair.',
            translation='May Allah bless you and shower His blessings upon you, and may He join you together in goodness.',
            reference='Abu Dawud, Tirmidhi',
            category=home,
            benefit='A dua to congratulate newlyweds and wish them a blessed marriage.'
        )

        Dua.objects.create(
            title='Dua for Traveling',
            arabic_text='اللَّهُ أَكْبَرُ، اللَّهُ أَكْبَرُ، اللَّهُ أَكْبَرُ، سُبْحَانَ الَّذِي سَخَّرَ لَنَا هَذَا وَمَا كُنَّا لَهُ مُقْرِنِينَ، وَإِنَّا إِلَى رَبِّنَا لَمُنْقَلِبُونَ، اللَّهُمَّ إِنَّا نَسْأَلُكَ فِي سَفَرِنَا هَذَا الْبِرَّ وَالتَّقْوَى، وَمِنَ الْعَمَلِ مَا تَرْضَى، اللَّهُمَّ هَوِّنْ عَلَيْنَا سَفَرَنَا هَذَا وَاطْوِ عَنَّا بُعْدَهُ، اللَّهُمَّ أَنْتَ الصَّاحِبُ فِي السَّفَرِ، وَالْخَلِيفَةُ فِي الْأَهْلِ، اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنْ وَعْثَاءِ السَّفَرِ، وَكَآبَةِ الْمَنْظَرِ، وَسُوءِ الْمُنْقَلَبِ فِي الْمَالِ وَالْأَهْلِ.',
            transliteration='Allahu Akbar, Allahu Akbar, Allahu Akbar. Subhanal-ladhi sakhkhara lana hadha wa ma kunna lahu muqrinin, wa inna ila Rabbina lamunqalibun. Allahumma inna nas\'aluka fi safarina hadha al-birra wat-taqwa, wa minal-\'amali ma tarda. Allahumma hawwin \'alayna safarana hadha, watwi \'anna bu\'dahu. Allahumma antas-sahibu fis-safar, wal-khalifatu fil-ahl. Allahumma inni a\'udhu bika min wa\'tha\'is-safar, wa kaabatil-manzar, wa su\'il-munqalabi fil-mali wal-ahl.',
            translation='Allah is the Greatest, Allah is the Greatest, Allah is the Greatest. Glory is to Him Who has provided this for us though we could never have had it by our efforts. Surely, unto our Lord we are returning. O Allah, we ask You on this our journey for goodness and piety, and for works that are pleasing to You. O Allah, lighten this journey for us and make its distance easy for us. O Allah, You are our Companion during the journey and the Guardian of the family. O Allah, I seek refuge in You from difficulties during the journey, from having a change of heart and being in a bad predicament, and I seek refuge in You from an ill-fated outcome with wealth and family.',
            reference='Muslim',
            category=travel,
            benefit='To be recited when embarking on a journey for protection and ease.'
        )

        Dua.objects.create(
            title='Dua for Protection (Ayatul Kursi)',
            arabic_text='اللَّهُ لاَ إِلَهَ إِلاَّ هُوَ الْحَيُّ الْقَيُّومُ، لاَ تَأْخُذُهُ سِنَةٌ وَلاَ نَوْمٌ، لَهُ مَا فِي السَّمَاوَاتِ وَمَا فِي الأَرْضِ، مَنْ ذَا الَّذِي يَشْفَعُ عِنْدَهُ إِلاَّ بِإِذْنِهِ، يَعْلَمُ مَا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ، وَلاَ يُحِيطُونَ بِشَيْءٍ مِنْ عِلْمِهِ إِلاَّ بِمَا شَاءَ، وَسِعَ كُرْسِيُّهُ السَّمَاوَاتِ وَالأَرْضَ، وَلاَ يَئُودُهُ حِفْظُهُمَا، وَهُوَ الْعَلِيُّ الْعَظِيمُ.',
            transliteration='Allahu la ilaha illa Huwal-Hayyul-Qayyum, la ta\'khudhuhu sinatun wa la nawm, lahu ma fis-samawati wa ma fil-\'ard, man dhal-ladhi yashfa\'u \'indahu illa bi\'idhnih, ya\'lamu ma bayna \'aydihim wa ma khalfahum, wa la yuhituna bishay\'im-min \'ilmihi illa bima sha\', wasi\'a kursiyyuhus-samawati wal-\'ard, wa la ya\'uduhu hifzuhuma, wa Huwal-\'Aliyyul-\'Azim.',
            translation='Allah - there is no deity except Him, the Ever-Living, the Sustainer of existence. Neither drowsiness overtakes Him nor sleep. To Him belongs whatever is in the heavens and whatever is on the earth. Who is it that can intercede with Him except by His permission? He knows what is before them and what will be after them, and they encompass not a thing of His knowledge except for what He wills. His Kursi extends over the heavens and the earth, and their preservation tires Him not. And He is the Most High, the Most Great.',
            reference='Quran 2:255',
            category=protection,
            benefit='Reading Ayatul Kursi before sleeping provides protection throughout the night.'
        )

        Dua.objects.create(
            title='Master of Seeking Forgiveness',
            arabic_text='اللَّهُمَّ أَنْتَ رَبِّي لاَ إِلَهَ إِلاَّ أَنْتَ، خَلَقْتَنِي وَأَنَا عَبْدُكَ، وَأَنَا عَلَى عَهْدِكَ وَوَعْدِكَ مَا اسْتَطَعْتُ، أَعُوذُ بِكَ مِنْ شَرِّ مَا صَنَعْتُ، أَبُوءُ لَكَ بِنِعْمَتِكَ عَلَيَّ، وَأَبُوءُ بِذَنْبِي فَاغْفِرْ لِي فَإِنَّهُ لاَ يَغْفِرُ الذُّنُوبَ إِلاَّ أَنْتَ.',
            transliteration='Allahumma anta Rabbi la ilaha illa anta, khalaqtani wa ana abduka, wa ana \'ala ahdika wa wa\'dika ma istata\'tu, a\'udhu bika min sharri ma sana\'tu, abu\'u laka bini\'matika \'alayya, wa abu\'u bidhanbi faghfir li fa innahu la yaghfirudh-dhunuba illa anta.',
            translation='O Allah, You are my Lord, there is no god but You, You created me and I am Your servant, and I abide by Your covenant and promise as best I can. I seek refuge in You from the evil of what I have done. I acknowledge before You Your blessings bestowed on me, and I confess my sins to You. Forgive me, for there is none who forgives sins except You.',
            reference='Bukhari',
            category=forgiveness,
            benefit='This is the master of seeking forgiveness. Whoever says it with firm belief during the day and dies before evening, or says it with firm belief during the night and dies before morning, will be among the people of Paradise.'
        )

        # Duas from JSON file
        Dua.objects.create(
            title='Dua before sleeping',
            arabic_text='بِاسْمِكَ اللَّهُمَّ أَمُوتُ وَأَحْيَا',
            transliteration='Bismika Allahumma amootu wa ahya',
            translation='In Your name, O Allah, I die and I live.',
            reference='Bukhari',
            category=sleeping,
            benefit='To be recited before sleeping for protection during the night.'
        )

        Dua.objects.create(
            title='Dua upon waking up',
            arabic_text='الْحَمْدُ لِلَّهِ الَّذِي أَحْيَانَا بَعْدَ مَا أَمَاتَنَا وَإِلَيْهِ النُّشُورُ',
            transliteration='Alhamdu lillahil-ladhi ahyana ba\'da ma amatana wa ilaihin-nushur',
            translation='Praise is to Allah Who gives us life after He has caused us to die and to Him is the return.',
            reference='Bukhari',
            category=sleeping,
            benefit='To be recited upon waking up as gratitude to Allah.'
        )

        Dua.objects.create(
            title='Dua when angry',
            arabic_text='أَعُوذُ بِاللَّهِ مِنَ الشَّيْطَانِ الرَّجِيمِ',
            transliteration='A\'udhu billahi minash-shaytanir-rajim',
            translation='I seek refuge with Allah from Satan, the accursed.',
            reference='Bukhari and Muslim',
            category=emotional,
            benefit='To be recited when feeling angry to control emotions.'
        )

        Dua.objects.create(
            title='Dua for Taraweeh',
            arabic_text='اللَّهُمَّ إِنِّي أَعُوذُ بِرِضَاكَ مِنْ سَخَطِكَ، وَبِمُعَافَاتِكَ مِنْ عُقُوبَتِكَ، وَأَعُوذُ بِكَ مِنْكَ، لَا أُحْصِي ثَنَاءً عَلَيْكَ، أَنْتَ كَمَا أَثْنَيْتَ عَلَى نَفْسِكَ',
            transliteration='Allahumma inni a\'udhu bi-ridaka min sakhatika, wa bi-mu\'afatika min \'uqubatika, wa a\'udhu bika minka, la uhsi thana\'an \'alayka, anta kama athnayta \'ala nafsika',
            translation='O Allah, I seek protection in Your pleasure from Your anger, and in Your forgiveness from Your punishment. I seek protection in You from You. I cannot count Your praises. You are as You have praised Yourself.',
            reference='Muslim',
            category=ramadan,
            benefit='To be recited during Taraweeh prayers in Ramadan.'
        )

        Dua.objects.create(
            title='Dua for entering the masjid',
            arabic_text='اللَّهُمَّ افْتَحْ لِي أَبْوَابَ رَحْمَتِكَ',
            transliteration='Allahumma iftah li abwaba rahmatika',
            translation='O Allah, open the gates of Your mercy for me.',
            reference='Muslim',
            category=masjid,
            benefit='To be recited when entering a mosque.'
        )

        Dua.objects.create(
            title='Dua for leaving the masjid',
            arabic_text='اللَّهُمَّ إِنِّي أَسْأَلُكَ مِنْ فَضْلِكَ',
            transliteration='Allahumma inni as\'aluka min fadlika',
            translation='O Allah, I ask You for Your bounty.',
            reference='Muslim',
            category=masjid,
            benefit='To be recited when leaving a mosque.'
        )

        Dua.objects.create(
            title='Dua before eating',
            arabic_text='بِسْمِ اللَّهِ',
            transliteration='Bismillah',
            translation='In the name of Allah.',
            reference='Abu Dawud',
            category=food,
            benefit='To be recited before starting to eat.'
        )

        Dua.objects.create(
            title='Dua after eating',
            arabic_text='الْحَمْدُ لِلَّهِ الَّذِي أَطْعَمَنِي هَذَا، وَرَزَقَنِيهِ، مِنْ غَيْرِ حَوْلٍ مِنِّي وَلَا قُوَّةٍ',
            transliteration='Alhamdu lillahil-ladhi at\'amani hadha, wa razaqanihi, min ghayri hawlin minni wa la quwwatin',
            translation='Praise is to Allah Who has fed me this and provided it for me without any might or power on my part.',
            reference='Abu Dawud, Tirmidhi',
            category=food,
            benefit='To be recited after finishing a meal as gratitude.'
        )

        Dua.objects.create(
            title='Dua for anxiety and sorrow',
            arabic_text='اللَّهُمَّ إِنِّي عَبْدُكَ، ابْنُ عَبْدِكَ، ابْنُ أَمَتِكَ، نَاصِيَتِي بِيَدِكَ، مَاضٍ فِيَّ حُكْمُكَ، عَدْلٌ فِيَّ قَضَاؤُكَ، أَسْأَلُكَ بِكُلِّ اسْمٍ هُوَ لَكَ، سَمَّيْتَ بِهِ نَفْسَكَ، أَوْ أَنْزَلْتَهُ فِي كِتَابِكَ، أَوْ عَلَّمْتَهُ أَحَدًا مِنْ خَلْقِكَ، أَوِ اسْتَأْثَرْتَ بِهِ فِي عِلْمِ الْغَيْبِ عِنْدَكَ، أَنْ تَجْعَلَ الْقُرْآنَ رَبِيعَ قَلْبِي، وَنُورَ صَدْرِي، وَجَلَاءَ حُزْنِي، وَذَهَابَ هَمِّي',
            transliteration='Allahumma inni \'abduka, ibnu \'abdika, ibnu amatika, nasiyati biyadika, madin fiyya hukmuka, \'adlun fiyya qada\'uka, as\'aluka bikulli ismin huwa laka, sammayta bihi nafsaka, aw anzaltahu fi kitabika, aw \'allamtahu ahadan min khalqika, aw ista\'tharta bihi fi \'ilmil-ghaybi \'indaka, an taj\'alal-Qur\'ana rabi\'a qalbi, wa nura sadri, wa jala\'a huzni, wa dhahaba hammi',
            translation='O Allah, I am Your slave, son of Your slave, son of Your maidservant, my forelock is in Your hand, Your command over me is forever executed and Your decree over me is just. I ask You by every name belonging to You which You named Yourself with, or revealed in Your Book, or You taught to any of Your creation, or You have preserved in the knowledge of the unseen with You, that You make the Quran the life of my heart and the light of my breast, and a departure for my sorrow and a release for my anxiety.',
            reference='Ahmad',
            category=emotional,
            benefit='A powerful dua for relieving anxiety, depression, and distress.'
        )

        Dua.objects.create(
            title='Sayyid-ul-Istighfar (The Master of Seeking Forgiveness)',
            arabic_text='اللَّهُمَّ أَنْتَ رَبِّي لَا إِلَهَ إِلَّا أَنْتَ، خَلَقْتَنِي وَأَنَا عَبْدُكَ، وَأَنَا عَلَى عَهْدِكَ وَوَعْدِكَ مَا اسْتَطَعْتُ، أَعُوذُ بِكَ مِنْ شَرِّ مَا صَنَعْتُ، أَبُوءُ لَكَ بِنِعْمَتِكَ عَلَيَّ، وَأَبُوءُ بِذَنْبِي فَاغْفِرْ لِي فَإِنَّهُ لَا يَغْفِرُ الذُّنُوبَ إِلَّا أَنْتَ',
            transliteration='Allahumma anta Rabbi la ilaha illa anta, Khalaqtani wa ana \'abduka, wa ana \'ala \'ahdika wa wa\'dika ma istata\'tu, A\'udhu bika min sharri ma sana\'tu, abu\'u laka bi ni\'matika \'alayya, wa abu\'u bi dhanbi faghfir li fa innahu la yaghfiru adh-dhunuba illa anta',
            translation='O Allah, You are my Lord, there is no god but You, You created me and I am Your servant, and I abide by Your covenant and promise as best I can, I seek refuge in You from the evil of what I have done, I acknowledge Your favor upon me, and I acknowledge my sin, so forgive me, for none forgives sins but You.',
            reference='Bukhari',
            category=forgiveness,
            benefit='This is the master of all prayers for seeking forgiveness.'
        )

        Dua.objects.create(
            title='Dua for protection (morning and evening)',
            arabic_text='بِسْمِ اللَّهِ الَّذِي لَا يَضُرُّ مَعَ اسْمِهِ شَيْءٌ فِي الْأَرْضِ وَلَا فِي السَّمَاءِ وَهُوَ السَّمِيعُ الْعَلِيمُ',
            transliteration='Bismillahil-ladhi la yadurru ma\'asmihi shay\'un fil-ardi wa la fis-sama\'i, wa huwas-Sami\'ul-\'Alim',
            translation='In the name of Allah with Whose name nothing can harm on earth or in heaven, and He is the All-Hearing, the All-Knowing.',
            reference='Abu Dawud, Tirmidhi',
            category=protection,
            benefit='To be recited three times in the morning and evening for protection.'
        )

        Dua.objects.create(
            title='Dua while breaking fast',
            arabic_text='ذَهَبَ الظَّمَأُ، وَابْتَلَّتِ الْعُرُوقُ، وَثَبَتَ الْأَجْرُ إِنْ شَاءَ اللَّهُ',
            transliteration='Dhahabazh-zhama\'u wabtallatil \'urooqu, wa thabatal-ajru insha\'Allah',
            translation='The thirst has gone, the veins are moistened, and the reward is confirmed, if Allah wills.',
            reference='Abu Dawud',
            category=ramadan,
            benefit='To be recited when breaking the fast during Ramadan.'
        )

        Dua.objects.create(
            title='Dua before starting Salah',
            arabic_text='سُبْحَانَكَ اللَّهُمَّ وَبِحَمْدِكَ، وَتَبَارَكَ اسْمُكَ، وَتَعَالَى جَدُّكَ، وَلَا إِلَهَ غَيْرُكَ',
            transliteration='Subhanakal-lahumma wa bihamdika, wa tabarakasmuka, wa ta\'ala jadduka, wa la ilaha ghayruk',
            translation='Glory is to You, O Allah, and praise, blessed is Your name, exalted is Your majesty, and there is no deity other than You.',
            reference='Abu Dawud, Tirmidhi',
            category=salah,
            benefit='To be recited after the opening takbeer of the prayer.'
        )
        Dua.objects.create(
            title='Dua for seeking guidance (Istikhara)',
            arabic_text='اللَّهُمَّ إِنِّي أَسْتَخِيرُكَ بِعِلْمِكَ، وَأَسْتَقْدِرُكَ بِقُدْرَتِكَ، وَأَسْأَلُكَ مِنْ فَضْلِكَ الْعَظِيمِ، فَإِنَّكَ تَقْدِرُ وَلاَ أَقْدِرُ، وَتَعْلَمُ وَلاَ أَعْلَمُ، وَأَنْتَ عَلاَّمُ الْغُيُوبِ...',
            transliteration='Allahumma inni astakhiruka bi ilmika, wa astaqdiruka bi qudratika, wa as\'aluka min fadlikal-azim...',
            translation='O Allah, I seek Your guidance by virtue of Your knowledge, and I seek ability by virtue of Your power...',
            reference='Bukhari',
            category=guidance,
            benefit='To be recited when making an important decision.'
        )

        Dua.objects.create(
            title='Dua for travelling',
            arabic_text='اللَّهُ أَكْبَرُ، اللَّهُ أَكْبَرُ، اللَّهُ أَكْبَرُ، سُبْحَانَ الَّذِي سَخَّرَ لَنَا هَذَا وَمَا كُنَّا لَهُ مُقْرِنِينَ...',
            transliteration='Allahu akbar, Allahu akbar, Allahu akbar. Subhanal-ladhi sakhkhara lana hadha...',
            translation='Allah is the Greatest, Allah is the Greatest, Allah is the Greatest. Glory to Him Who has provided this for us...',
            reference='Muslim',
            category=travel,
            benefit='To be recited before setting out on a journey for protection and ease.'
        )

        Dua.objects.create(
            title='Dua e Qunoot (Shafi)',
            arabic_text='no arabic at the moment',
            transliteration='Allahumma ihdini feeman hadayt, wa a’fini fiman afait, wa tawallani fiman tawallait...',
            translation='O Allah, guide me among those You have guided, pardon me among those You have pardoned...',
            reference='At-Tirmidhi: 464, Abu Dawud: 1425',
            category=witr,
            benefit='Recited in Witr prayer by followers of the Shafi school.'
        )

        Dua.objects.create(
            title='Dua e Qunoot (Hanafi)',
            arabic_text='كِۡ نَسْتَعِينُ وَنَسْتَغْفِرُكَ وَنُؤْمِنُ بِكَ...',
            transliteration='Allah humma inna nasta-eenoka wa nastaghfiruka wa nu\'minu bika wa natawakkalu alaika...',
            translation='O Allah! We implore You for help and beg forgiveness of You and believe in You and rely on You...',
            reference='As-Sunan Kubra lil-Bayhaqi 2/201',
            category=witr,
            benefit='Recited in Witr prayer by followers of the Hanafi school.'
        )


        self.stdout.write(self.style.SUCCESS('Successfully populated the database with additional duas.'))
