import { useState } from 'react'
import { 
  Home, 
  Users, 
  ShoppingBag, 
  Package, 
  CreditCard, 
  Settings,
  Menu,
  X,
  LogOut
} from 'lucide-react'
import { Button } from '@/components/ui/button'

const Sidebar = ({ activeSection, setActiveSection }) => {
  const [isCollapsed, setIsCollapsed] = useState(false)

  const menuItems = [
    { id: 'dashboard', label: 'لوحة التحكم', icon: Home },
    { id: 'users', label: 'إدارة المستخدمين', icon: Users },
    { id: 'services', label: 'إدارة الخدمات', icon: Package },
    { id: 'orders', label: 'إدارة الطلبات', icon: ShoppingBag },
    { id: 'transactions', label: 'المعاملات المالية', icon: CreditCard },
    { id: 'settings', label: 'الإعدادات', icon: Settings },
  ]

  return (
    <div className={`bg-gray-900 text-white h-screen transition-all duration-300 ${
      isCollapsed ? 'w-16' : 'w-64'
    } flex flex-col`}>
      {/* Header */}
      <div className="p-4 border-b border-gray-700 flex items-center justify-between">
        {!isCollapsed && (
          <h2 className="text-xl font-bold text-blue-400">Followers Store</h2>
        )}
        <Button
          variant="ghost"
          size="sm"
          onClick={() => setIsCollapsed(!isCollapsed)}
          className="text-white hover:bg-gray-700"
        >
          {isCollapsed ? <Menu size={20} /> : <X size={20} />}
        </Button>
      </div>

      {/* Navigation */}
      <nav className="flex-1 p-4">
        <ul className="space-y-2">
          {menuItems.map((item) => {
            const Icon = item.icon
            return (
              <li key={item.id}>
                <button
                  onClick={() => setActiveSection(item.id)}
                  className={`w-full flex items-center gap-3 p-3 rounded-lg transition-colors ${
                    activeSection === item.id
                      ? 'bg-blue-600 text-white'
                      : 'text-gray-300 hover:bg-gray-700 hover:text-white'
                  }`}
                >
                  <Icon size={20} />
                  {!isCollapsed && <span>{item.label}</span>}
                </button>
              </li>
            )
          })}
        </ul>
      </nav>

      {/* Footer */}
      <div className="p-4 border-t border-gray-700">
        <Button
          variant="ghost"
          className="w-full flex items-center gap-3 text-gray-300 hover:bg-gray-700 hover:text-white"
        >
          <LogOut size={20} />
          {!isCollapsed && <span>تسجيل الخروج</span>}
        </Button>
      </div>
    </div>
  )
}

export default Sidebar

