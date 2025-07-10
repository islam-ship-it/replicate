import { Button } from '@/components/ui/button'
import { ArrowLeft, Star, Users, Zap } from 'lucide-react'
import heroImage from '../assets/social-media-hero.png'

const Hero = () => {
  return (
    <section className="bg-gradient-to-br from-blue-50 to-indigo-100 py-20 lg:py-32">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          {/* Content */}
          <div className="text-center lg:text-right">
            <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold text-gray-900 leading-tight">
              عزز حضورك على
              <span className="text-blue-600 block">السوشيال ميديا</span>
            </h1>
            <p className="mt-6 text-xl text-gray-600 leading-relaxed">
              احصل على متابعين حقيقيين، لايكات، ومشاهدات لجميع منصات التواصل الاجتماعي. 
              خدمات سريعة وآمنة وبأسعار تنافسية.
            </p>
            
            {/* Features */}
            <div className="mt-8 flex flex-wrap justify-center lg:justify-start gap-6">
              <div className="flex items-center text-gray-700">
                <Zap className="w-5 h-5 text-blue-600 mr-2" />
                <span className="text-sm font-medium">تنفيذ سريع</span>
              </div>
              <div className="flex items-center text-gray-700">
                <Users className="w-5 h-5 text-blue-600 mr-2" />
                <span className="text-sm font-medium">متابعين حقيقيين</span>
              </div>
              <div className="flex items-center text-gray-700">
                <Star className="w-5 h-5 text-blue-600 mr-2" />
                <span className="text-sm font-medium">جودة عالية</span>
              </div>
            </div>

            {/* CTA Buttons */}
            <div className="mt-10 flex flex-col sm:flex-row gap-4 justify-center lg:justify-start">
              <Button size="lg" className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 text-lg">
                ابدأ الآن
                <ArrowLeft className="w-5 h-5 mr-2" />
              </Button>
              <Button variant="outline" size="lg" className="border-blue-600 text-blue-600 hover:bg-blue-50 px-8 py-3 text-lg">
                تصفح الخدمات
              </Button>
            </div>

            {/* Stats */}
            <div className="mt-12 grid grid-cols-3 gap-6 text-center lg:text-right">
              <div>
                <div className="text-2xl font-bold text-blue-600">10K+</div>
                <div className="text-sm text-gray-600">عميل راضي</div>
              </div>
              <div>
                <div className="text-2xl font-bold text-blue-600">50K+</div>
                <div className="text-sm text-gray-600">طلب منجز</div>
              </div>
              <div>
                <div className="text-2xl font-bold text-blue-600">24/7</div>
                <div className="text-sm text-gray-600">دعم فني</div>
              </div>
            </div>
          </div>

          {/* Image */}
          <div className="relative">
            <div className="relative z-10">
              <img
                src={heroImage}
                alt="Social Media Marketing"
                className="w-full h-auto rounded-2xl shadow-2xl"
              />
            </div>
            {/* Background decoration */}
            <div className="absolute -top-4 -right-4 w-full h-full bg-blue-200 rounded-2xl -z-10"></div>
            <div className="absolute -bottom-4 -left-4 w-full h-full bg-orange-200 rounded-2xl -z-20"></div>
          </div>
        </div>
      </div>
    </section>
  )
}

export default Hero

