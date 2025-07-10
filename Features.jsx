import { Shield, Zap, Users, Headphones, CreditCard, TrendingUp } from 'lucide-react'

const Features = () => {
  const features = [
    {
      icon: Zap,
      title: 'تنفيذ سريع',
      description: 'نبدأ تنفيذ طلبك خلال دقائق من التأكيد، مع ضمان السرعة والجودة.',
      color: 'text-yellow-600',
      bgColor: 'bg-yellow-50'
    },
    {
      icon: Shield,
      title: 'آمان مضمون',
      description: 'جميع خدماتنا آمنة 100% ولا تعرض حسابك للخطر أو الحظر.',
      color: 'text-green-600',
      bgColor: 'bg-green-50'
    },
    {
      icon: Users,
      title: 'متابعين حقيقيين',
      description: 'نوفر متابعين حقيقيين ونشطين، وليس حسابات وهمية أو بوتات.',
      color: 'text-blue-600',
      bgColor: 'bg-blue-50'
    },
    {
      icon: Headphones,
      title: 'دعم 24/7',
      description: 'فريق الدعم الفني متاح على مدار الساعة لمساعدتك وحل أي استفسار.',
      color: 'text-purple-600',
      bgColor: 'bg-purple-50'
    },
    {
      icon: CreditCard,
      title: 'دفع آمن',
      description: 'طرق دفع متعددة وآمنة مع حماية كاملة لبياناتك المالية.',
      color: 'text-indigo-600',
      bgColor: 'bg-indigo-50'
    },
    {
      icon: TrendingUp,
      title: 'نتائج مضمونة',
      description: 'نضمن لك تحقيق النتائج المطلوبة أو استرداد أموالك كاملة.',
      color: 'text-red-600',
      bgColor: 'bg-red-50'
    }
  ]

  return (
    <section className="py-20 bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="text-center mb-16">
          <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
            لماذا تختارنا؟
          </h2>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            نحن نقدم أفضل خدمات السوشيال ميديا مع ضمان الجودة والأمان
          </p>
        </div>

        {/* Features Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {features.map((feature, index) => (
            <div
              key={index}
              className="bg-white rounded-xl p-8 shadow-sm hover:shadow-md transition-shadow duration-300"
            >
              <div className={`${feature.bgColor} w-16 h-16 rounded-lg flex items-center justify-center mb-6`}>
                <feature.icon className={`w-8 h-8 ${feature.color}`} />
              </div>
              <h3 className="text-xl font-semibold text-gray-900 mb-4">
                {feature.title}
              </h3>
              <p className="text-gray-600 leading-relaxed">
                {feature.description}
              </p>
            </div>
          ))}
        </div>

        {/* Stats Section */}
        <div className="mt-20 bg-white rounded-2xl p-8 md:p-12 shadow-sm">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
            <div>
              <div className="text-3xl md:text-4xl font-bold text-blue-600 mb-2">
                10,000+
              </div>
              <div className="text-gray-600 font-medium">عميل راضي</div>
            </div>
            <div>
              <div className="text-3xl md:text-4xl font-bold text-blue-600 mb-2">
                50,000+
              </div>
              <div className="text-gray-600 font-medium">طلب منجز</div>
            </div>
            <div>
              <div className="text-3xl md:text-4xl font-bold text-blue-600 mb-2">
                99.9%
              </div>
              <div className="text-gray-600 font-medium">معدل النجاح</div>
            </div>
            <div>
              <div className="text-3xl md:text-4xl font-bold text-blue-600 mb-2">
                24/7
              </div>
              <div className="text-gray-600 font-medium">دعم فني</div>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}

export default Features

