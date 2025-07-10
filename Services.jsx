import { Button } from '@/components/ui/button'
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from '@/components/ui/card'
import { Instagram, Youtube, Twitter, Heart, Eye, Users, TrendingUp } from 'lucide-react'

const Services = () => {
  const services = [
    {
      id: 1,
      platform: 'Instagram',
      icon: Instagram,
      color: 'text-pink-600',
      bgColor: 'bg-pink-50',
      services: [
        { type: 'متابعين', icon: Users, price: '5', description: 'متابعين حقيقيين وآمنين' },
        { type: 'لايكات', icon: Heart, price: '2', description: 'لايكات سريعة وطبيعية' },
        { type: 'مشاهدات', icon: Eye, price: '1', description: 'مشاهدات عالية الجودة' }
      ]
    },
    {
      id: 2,
      platform: 'TikTok',
      icon: TrendingUp,
      color: 'text-black',
      bgColor: 'bg-gray-50',
      services: [
        { type: 'متابعين', icon: Users, price: '4', description: 'متابعين نشطين ومتفاعلين' },
        { type: 'لايكات', icon: Heart, price: '1.5', description: 'لايكات سريعة التنفيذ' },
        { type: 'مشاهدات', icon: Eye, price: '0.5', description: 'مشاهدات حقيقية ومضمونة' }
      ]
    },
    {
      id: 3,
      platform: 'YouTube',
      icon: Youtube,
      color: 'text-red-600',
      bgColor: 'bg-red-50',
      services: [
        { type: 'مشتركين', icon: Users, price: '8', description: 'مشتركين حقيقيين ومهتمين' },
        { type: 'لايكات', icon: Heart, price: '3', description: 'لايكات طبيعية ومتدرجة' },
        { type: 'مشاهدات', icon: Eye, price: '2', description: 'مشاهدات عالية الاحتفاظ' }
      ]
    },
    {
      id: 4,
      platform: 'Twitter',
      icon: Twitter,
      color: 'text-blue-500',
      bgColor: 'bg-blue-50',
      services: [
        { type: 'متابعين', icon: Users, price: '6', description: 'متابعين نشطين ومتنوعين' },
        { type: 'لايكات', icon: Heart, price: '2.5', description: 'لايكات سريعة وآمنة' },
        { type: 'ريتويت', icon: TrendingUp, price: '3', description: 'إعادة تغريد طبيعية' }
      ]
    }
  ]

  return (
    <section id="services" className="py-20 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="text-center mb-16">
          <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
            خدماتنا المميزة
          </h2>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            نقدم خدمات شاملة لجميع منصات التواصل الاجتماعي بأعلى جودة وأفضل الأسعار
          </p>
        </div>

        {/* Services Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          {services.map((platform) => (
            <div key={platform.id} className="space-y-4">
              {/* Platform Header */}
              <div className={`${platform.bgColor} rounded-lg p-4 text-center`}>
                <platform.icon className={`w-8 h-8 ${platform.color} mx-auto mb-2`} />
                <h3 className="text-lg font-semibold text-gray-900">{platform.platform}</h3>
              </div>

              {/* Platform Services */}
              <div className="space-y-3">
                {platform.services.map((service, index) => (
                  <Card key={index} className="hover:shadow-md transition-shadow">
                    <CardHeader className="pb-3">
                      <div className="flex items-center justify-between">
                        <div className="flex items-center">
                          <service.icon className="w-5 h-5 text-gray-600 mr-2" />
                          <CardTitle className="text-sm">{service.type}</CardTitle>
                        </div>
                        <span className="text-lg font-bold text-blue-600">${service.price}</span>
                      </div>
                      <CardDescription className="text-xs">
                        {service.description}
                      </CardDescription>
                    </CardHeader>
                    <CardFooter className="pt-0">
                      <Button size="sm" className="w-full bg-blue-600 hover:bg-blue-700 text-white">
                        اطلب الآن
                      </Button>
                    </CardFooter>
                  </Card>
                ))}
              </div>
            </div>
          ))}
        </div>

        {/* CTA */}
        <div className="text-center mt-16">
          <p className="text-gray-600 mb-6">
            لا تجد الخدمة التي تبحث عنها؟
          </p>
          <Button size="lg" variant="outline" className="border-blue-600 text-blue-600 hover:bg-blue-50">
            تصفح جميع الخدمات
          </Button>
        </div>
      </div>
    </section>
  )
}

export default Services

