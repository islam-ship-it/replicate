import { Star, Quote } from 'lucide-react'
import { Card, CardContent } from '@/components/ui/card'

const Testimonials = () => {
  const testimonials = [
    {
      id: 1,
      name: 'أحمد محمد',
      role: 'مؤثر على انستقرام',
      content: 'خدمة ممتازة! حصلت على 10,000 متابع حقيقي خلال أسبوع واحد. الجودة عالية والأسعار معقولة جداً.',
      rating: 5,
      avatar: '👨‍💼'
    },
    {
      id: 2,
      name: 'فاطمة العلي',
      role: 'صاحبة متجر إلكتروني',
      content: 'ساعدوني في زيادة مبيعاتي بشكل كبير من خلال زيادة المتابعين والتفاعل. أنصح بهم بشدة!',
      rating: 5,
      avatar: '👩‍💻'
    },
    {
      id: 3,
      name: 'خالد السعيد',
      role: 'يوتيوبر',
      content: 'أفضل موقع جربته لزيادة المشتركين في اليوتيوب. الخدمة سريعة والدعم الفني ممتاز.',
      rating: 5,
      avatar: '🎬'
    },
    {
      id: 4,
      name: 'نورا أحمد',
      role: 'مدونة',
      content: 'تعاملت معهم عدة مرات وكانت التجربة رائعة في كل مرة. متابعين حقيقيين ونتائج مضمونة.',
      rating: 5,
      avatar: '✍️'
    },
    {
      id: 5,
      name: 'محمد الحربي',
      role: 'رجل أعمال',
      content: 'ساعدوني في بناء حضور قوي لشركتي على السوشيال ميديا. خدمة احترافية وأسعار تنافسية.',
      rating: 5,
      avatar: '💼'
    },
    {
      id: 6,
      name: 'سارة الزهراني',
      role: 'مصممة جرافيك',
      content: 'زادت متابعيني بشكل طبيعي وآمن. لم أواجه أي مشاكل مع حسابي والنتائج كانت أفضل من المتوقع.',
      rating: 5,
      avatar: '🎨'
    }
  ]

  const renderStars = (rating) => {
    return Array.from({ length: 5 }, (_, index) => (
      <Star
        key={index}
        className={`w-4 h-4 ${
          index < rating ? 'text-yellow-400 fill-current' : 'text-gray-300'
        }`}
      />
    ))
  }

  return (
    <section className="py-20 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="text-center mb-16">
          <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
            ماذا يقول عملاؤنا؟
          </h2>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            آراء حقيقية من عملائنا الذين حققوا نجاحاً باهراً معنا
          </p>
        </div>

        {/* Testimonials Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {testimonials.map((testimonial) => (
            <Card key={testimonial.id} className="hover:shadow-lg transition-shadow duration-300">
              <CardContent className="p-6">
                {/* Quote Icon */}
                <Quote className="w-8 h-8 text-blue-600 mb-4" />
                
                {/* Content */}
                <p className="text-gray-700 mb-6 leading-relaxed">
                  "{testimonial.content}"
                </p>
                
                {/* Rating */}
                <div className="flex items-center mb-4">
                  {renderStars(testimonial.rating)}
                </div>
                
                {/* Author */}
                <div className="flex items-center">
                  <div className="text-2xl mr-3">
                    {testimonial.avatar}
                  </div>
                  <div>
                    <div className="font-semibold text-gray-900">
                      {testimonial.name}
                    </div>
                    <div className="text-sm text-gray-600">
                      {testimonial.role}
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>

        {/* Overall Rating */}
        <div className="mt-16 text-center">
          <div className="bg-blue-50 rounded-2xl p-8 inline-block">
            <div className="flex items-center justify-center mb-4">
              {renderStars(5)}
              <span className="text-2xl font-bold text-gray-900 mr-3">5.0</span>
            </div>
            <p className="text-gray-700 font-medium">
              متوسط التقييم من أكثر من 10,000 عميل راضي
            </p>
          </div>
        </div>
      </div>
    </section>
  )
}

export default Testimonials

